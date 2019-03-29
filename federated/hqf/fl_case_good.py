from six.moves import range
import tensorflow as tf
from tensorflow_federated import python as tff
from tensorflow.python.keras.optimizer_v2 import gradient_descent
import collections 

tf.compat.v1.enable_v2_behavior()

# Load simulation data.
source, _ = tff.simulation.datasets.emnist.load_data()

def preprocess(dataset):

  def element_fn(element):
    return collections.OrderedDict([
        ('x', tf.reshape(element['pixels'], [-1])),
        ('y', tf.reshape(element['label'], [1])),
    ])

  return dataset.repeat(10).map(element_fn).shuffle(
      500).batch(20)

def make_federated_data(client_data, client_ids):
  return [preprocess(client_data.create_tf_dataset_for_client(x))
          for x in client_ids]

sample_clients = source.client_ids[0:3]

sample_batch = make_federated_data(source, sample_clients)

def create_compiled_keras_model():
  model = tf.keras.models.Sequential([
      tf.keras.layers.Dense(
          10, activation=tf.nn.softmax, kernel_initializer='zeros', input_shape=(784,))])
  
  def loss_fn(y_true, y_pred):
    return tf.reduce_mean(tf.keras.losses.sparse_categorical_crossentropy(
        y_true, y_pred))
 
  model.compile(
      loss=loss_fn,
      optimizer=gradient_descent.SGD(learning_rate=0.02),
      metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
  return model

example_dataset = source.create_tf_dataset_for_client(
    source.client_ids[0])
preprocessed_example_dataset = preprocess(example_dataset)

sample = tf.contrib.framework.nest.map_structure(
    lambda x: x.numpy(), iter(preprocessed_example_dataset).next())

# Wrap a Keras model for use with TFF.
def model_fn():
  keras_model = create_compiled_keras_model()
  return tff.learning.from_compiled_keras_model(keras_model, 
                               sample)

# Simulate a few rounds of training with the selected client devices.
trainer = tff.learning.build_federated_averaging_process(model_fn)
state = trainer.initialize()
for _ in range(5):
  state, metrics = trainer.next(state, sample_batch)
  print (metrics.loss)


