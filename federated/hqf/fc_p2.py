from __future__ import absolute_import, division, print_function

import collections
import numpy as np
from six.moves import range
import tensorflow as tf

from tensorflow_federated import python as tff

tf.compat.v1.enable_v2_behavior()


@tff.federated_computation
def hello_world():
  return 'Hello, World!'


hello_world()

#@test {"output": "ignore"}
mnist_train, mnist_test = tf.keras.datasets.mnist.load_data()


[(x.dtype, x.shape) for x in mnist_train]


NUM_EXAMPLES_PER_USER = 1000
BATCH_SIZE = 100

def get_data_for_digit(source, digit):
  output_sequence = []
  all_samples = [i for i, d in enumerate(source[1]) if d == digit]
  for i in range(0, min(len(all_samples), NUM_EXAMPLES_PER_USER), BATCH_SIZE):
    batch_samples = all_samples[i:i + BATCH_SIZE]
    output_sequence.append({
        'x': np.array([source[0][i].flatten() / 255.0 for i in batch_samples],
                      dtype=np.float32),
        'y': np.array([source[1][i] for i in batch_samples], dtype=np.int32)})
  return output_sequence

federated_train_data = [get_data_for_digit(mnist_train, d) for d in range(10)]

federated_test_data = [get_data_for_digit(mnist_test, d) for d in range(10)]


BATCH_TYPE = tff.NamedTupleType([
    ('x', tff.TensorType(tf.float32, [None, 784])),
    ('y', tff.TensorType(tf.int32, [None]))])


MODEL_TYPE = tff.NamedTupleType([
    ('weights', tff.TensorType(tf.float32, [784, 10])),
    ('bias', tff.TensorType(tf.float32, [10]))])



@tff.tf_computation(MODEL_TYPE, BATCH_TYPE)
def batch_loss(model, batch):
  predicted_y = tf.nn.softmax(tf.matmul(batch.x, model.weights) + model.bias)
  return -tf.reduce_mean(tf.reduce_sum(
      tf.one_hot(batch.y, 10) * tf.log(predicted_y), reduction_indices=[1]))



initial_model = {
    'weights': np.zeros([784, 10], dtype=np.float32),
    'bias': np.zeros([10], dtype=np.float32)
}

sample_batch = federated_train_data[5][-1]

batch_loss(initial_model, sample_batch)


@tff.tf_computation(MODEL_TYPE, BATCH_TYPE, tf.float32)
def batch_train(initial_model, batch, learning_rate):
  # Define a group of model variables and set them to `initial_model`.
  model_vars = tff.utils.get_variables('v', MODEL_TYPE)
  init_model = tff.utils.assign(model_vars, initial_model)
  # Perform one step of gradient descent using loss from `batch_loss`.
  optimizer = tf.train.GradientDescentOptimizer(learning_rate)
  with tf.control_dependencies([init_model]):
  	train_model = optimizer.minimize(batch_loss(model_vars, batch))
  # Return the model vars after performing this gradient descent step.
  with tf.control_dependencies([train_model]):
  	return tff.utils.identity(model_vars)


LOCAL_DATA_TYPE = tff.SequenceType(BATCH_TYPE)

@tff.federated_computation(MODEL_TYPE, tf.float32, LOCAL_DATA_TYPE)
def local_train(initial_model, learning_rate, all_batches):
  # Mapping function to apply to each batch.
  @tff.federated_computation(MODEL_TYPE, BATCH_TYPE)
  def batch_fn(model, batch):
  	return batch_train(model, batch, learning_rate)
  return tff.sequence_reduce(all_batches, initial_model, batch_fn)



model = initial_model
losses = []
for _ in range(5):
  model = batch_train(model, sample_batch, 0.1)
  losses.append(batch_loss(model, sample_batch))



locally_trained_model = local_train(initial_model, 0.1, federated_train_data[5])



@tff.federated_computation(MODEL_TYPE, LOCAL_DATA_TYPE)
def local_eval(model, all_batches):
  # TODO(b/120157713): Replace with `tff.sequence_average()` once implemented.
  return tff.sequence_sum(
      tff.sequence_map(
          tff.federated_computation(lambda b: batch_loss(model, b), BATCH_TYPE),
          all_batches))



SERVER_MODEL_TYPE = tff.FederatedType(MODEL_TYPE, tff.SERVER, all_equal=True)
CLIENT_DATA_TYPE = tff.FederatedType(LOCAL_DATA_TYPE, tff.CLIENTS)


@tff.federated_computation(SERVER_MODEL_TYPE, CLIENT_DATA_TYPE)
def federated_eval(model, data):
	return tff.federated_mean(
      tff.federated_map(local_eval, [tff.federated_broadcast(model), data]))


SERVER_FLOAT_TYPE = tff.FederatedType(tf.float32, tff.SERVER, all_equal=True)

@tff.federated_computation(
    SERVER_MODEL_TYPE, SERVER_FLOAT_TYPE, CLIENT_DATA_TYPE)
def federated_train(model, learning_rate, data):
	return tff.federated_mean(
      tff.federated_map(
          local_train,
          [tff.federated_broadcast(model),
           tff.federated_broadcast(learning_rate),
           data]))


model = initial_model
learning_rate = 0.1
for round_num in range(5):
  model = federated_train(model, learning_rate, federated_train_data)
  learning_rate = learning_rate * 0.9
  loss = federated_eval(model, federated_train_data)
  print('round {}, loss={}'.format(round_num, loss))


print('initial_model test loss =', federated_eval(initial_model, federated_test_data))
print('trained_model test loss =', federated_eval(model, federated_test_data))



