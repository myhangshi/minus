import zmq
import time
import json
import numpy as np

portREP = "5555"
portPUB = "5556"

# Prepare 0MQ context and sockets
context = zmq.Context()

# Socket to receive parameter from edge devices(nodes)
receiver =  context.socket(zmq.REP)
receiver.setsockopt(zmq.LINGER, 0)
receiver.bind("tcp://*:%s" % portREP)

# Socket to send parameters to edge devices(nodes)
publisher = context.socket(zmq.PUB)
# set SNDHWM, so we don't drop messages for slow subscribers
publisher.sndhwm = 1100000
publisher.bind("tcp://*:%s" % portPUB)

def main():
    parameter_queue = [] #queue to store parameters from edge nodes.
    num_clients = 0
    while True:
        try:
            if num_clients < 2:
                msg = receiver.recv()
                num_clients += 1
                parameter_queue.append(msg)
                #print(len(parameter_queue))
                #time.sleep(1) #for testing only
                # send synchronization reply
                #receiver.send(b'')
                receiver.send(b'test')
            #send aggregated parameters to the edge nodes.
            else:
                params = aggregatedparams(parameter_queue)
                publish(params) #publish aggregated parameters 
                parameter_queue = [] 
                num_clients = 0
        except KeyboardInterrupt:
            break

def aggregatedparams(parameter_queue):
    #for params in parameter_queue:
    for i in range(0, len(parameter_queue)):
        params = parameter_queue[i]
        params = json.loads(params)
        for p in params:
            params[p] = np.asarray(params[p])
        #print params
        parameter_queue[i] = params
    mean_params = {k: (sum(params[k] for params in parameter_queue) /
                        len(parameter_queue))
                    for k in parameter_queue[0]}
    for k in params:
        mean_params[k] = mean_params[k].tolist()
    for k in mean_params: print k
    return mean_params

def publish(params):
    msg = json.dumps(params)
    topic = 1
    publisher.send("%d %s" % (topic, msg))

if __name__ == "__main__":
    main()
