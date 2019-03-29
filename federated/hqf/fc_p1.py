from __future__ import absolute_import, division, print_function

import numpy as np
from six.moves import range
import tensorflow as tf

from tensorflow_federated import python as tff

tf.enable_resource_variables()



######prelude#########
######################

@tff.federated_computation(tff.FederatedType(tf.float32, tff.CLIENTS))
def get_average_temperature(sensor_readings):
  return tff.federated_mean(sensor_readings)


@tff.federated_computation(tff.FederatedType(tf.float32, tff.CLIENTS))
def get_average_temperature(sensor_readings):

  print ('Getting traced, the argument is "{}".'.format(
      type(sensor_readings).__name__))

  return tff.federated_average(sensor_readings)

####################
####################

@tff.tf_computation(tf.float32)
def add_half(x):
  return tf.add(x, 0.5)


@tff.federated_computation(tff.FederatedType(tf.float32, tff.CLIENTS))
def add_half_on_clients(x):
  return tff.federated_map(add_half, x)

####################
####################

@tff.tf_computation(tff.SequenceType(tf.int32))
def foo(x):
  return x.reduce(np.int32(0), lambda x, y: x + y)

foo([1, 2, 3])


####################
####################

@tff.tf_computation(tff.SequenceType([('A', tf.int32), ('B', tf.int32)]))
def foo(ds):
  print ('output_types = {}, shapes = {}'.format(
      ds.output_types, ds.output_shapes))
  return ds.reduce(np.int32(0), lambda total, x: total + x['A'] * x['B'])


foo([{'A': 2, 'B': 3}, {'A': 4, 'B': 5}])



####################
####################


@tff.tf_computation(tff.SequenceType(tf.float32))
def get_local_temperature_average(local_temperatures):
  sum_and_count = (
      local_temperatures.reduce((0.0, 0), lambda x, y: (x[0] + y, x[1] + 1)))
  return sum_and_count[0] / tf.to_float(sum_and_count[1])

get_local_temperature_average([68.5, 70.3, 69.8])



@tff.federated_computation(
    tff.FederatedType(tff.SequenceType(tf.float32), tff.CLIENTS))
def get_global_temperature_average(sensor_readings):
  return tff.federated_mean(
      tff.federated_map(get_local_temperature_average, sensor_readings))


get_global_temperature_average([[68.0, 70.0], [71.0], [68.0, 72.0, 70.0]])


