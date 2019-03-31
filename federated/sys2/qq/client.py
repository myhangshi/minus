import zmq

# Prepare 0MQ context and sockets
context = zmq.Context()

# receiver to send param to server and get acknowledgement back.
receiver = context.socket(zmq.REQ)
#receiver = context.socket(zmq.DEALER) #TODO change REQ to DEALER
receiver.connect("tcp://localhost:5555")

# Subscribe to parameters published by the server
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
subscriber.setsockopt(zmq.SUBSCRIBE, b"1")

# Initialize poll set -- to read from both the sockets.
poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)
poller.register(subscriber, zmq.POLLIN)

init = False 

# Process messages from both sockets
while True:
    #For REQ-REP send the first message here
    if not init:
        receiver.send(b'NODE1')
        init = True
    try:
       socks = dict(poller.poll())
    except KeyboardInterrupt:
       break

    if receiver in socks:
        #Check for ACK 
        message = receiver.recv()
        print(message)

    if subscriber in socks:
        #get model params from the server and load them into the local model here.
        message = subscriber.recv()
        print(message)
        receiver.send(b'NODE1')
