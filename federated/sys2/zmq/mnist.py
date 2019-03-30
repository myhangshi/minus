from __future__ import print_function
import argparse
import numpy as np
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import transforms
import json
import zmq
import datasets

# Prepare 0MQ context and sockets
context = zmq.Context()

# receiver to send param to server and get acknowledgement back.
receiver = context.socket(zmq.REQ)
receiver.connect("tcp://10.145.254.121:5555")

# Subscribe to parameters published by the server
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://10.145.254.121:5556")
subscriber.setsockopt(zmq.SUBSCRIBE, b"1")

# Initialize poll set -- to read from both the sockets.
poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)
poller.register(subscriber, zmq.POLLIN)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5, 1)
        self.conv2 = nn.Conv2d(20, 50, 5, 1)
        self.fc1 = nn.Linear(4*4*50, 500)
        self.fc2 = nn.Linear(500, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 4*4*50)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
    
class MNISTTrainActor(object):
    """Simple actor for MNIST trainer."""
    def __init__(self):
        #print("Initialize Actor environment gpu id: ", os.environ["CUDA_VISIBLE_DEVICES"])
        #self.device = torch.device("cuda")
        self.device = torch.device("cpu")
        self.model = Net().to(self.device)
        #self.parameterserver = ps

        kwargs = {'num_workers': 1, 'pin_memory': True}
        self.train_loader = torch.utils.data.DataLoader(
            datasets.MNIST('/data/mnist', train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])),
            batch_size=64, shuffle=True, **kwargs)
        self.test_loader = torch.utils.data.DataLoader(
        datasets.MNIST('/data/mnist', train=False, transform=transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])),
        batch_size=1000, shuffle=True, **kwargs)

        momentum = 0.5
        lr = 0.01
        self.optimizer = optim.SGD(self.model.parameters(), lr=lr, momentum=momentum)

        self.id = 0 
        print("ID: ", self.id) 

    #def run_train(self, weights):
    def run_train(self):
        #self.model.load_state_dict(weights)
        #self.model.cuda()
        print("starting run_train for actor.id = ", self.id)
        for batch_idx, (data, target) in enumerate(self.train_loader):
            #send even batches to id == 1 and odd to id == 0
            #if (self.id % 2 == 0): continue
            if ((self.id % 2 == 0 and batch_idx % 2 == 0) or
                (self.id % 2 == 1 and batch_idx % 2 == 1)) : continue
            #print("batch_idx, self.id", batch_idx, self.id)
            data, target = data.to(self.device), target.to(self.device)
            self.optimizer.zero_grad()
            output = self.model(data)
            loss = F.nll_loss(output, target)
            loss.backward()
            self.optimizer.step()
            #if ((batch_idx % 200 == 0 and self.id % 2 == 0) or 
            #    (batch_idx % 201 == 0 and self.id % 2 == 1)):
            if batch_idx % 200 == 0 or batch_idx % 201 == 0:
                print('Actor ID: {} batch_idx: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    self.id, batch_idx, batch_idx * len(data), len(self.train_loader.dataset),
                    100. * batch_idx / len(self.train_loader), loss.item()))
                #logging.info('Actor ID: %s', self.id)
        weights = self.model.cpu().state_dict()
        return weights

    def run_test(self):
        #model.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in self.test_loader:
                data, target = data.to(self.device), target.to(self.device)
                output = self.model(data)
                test_loss += F.nll_loss(output, target).item() # sum up batch loss
                pred = output.max(1, keepdim=True)[1] # get the index of the max log-probability
                correct += pred.eq(target.view_as(pred)).sum().item()

        test_loss /= len(self.test_loader.dataset)

        print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
            test_loss, correct, len(self.test_loader.dataset),
            100. * correct / len(self.test_loader.dataset)))

    def get_weights(self):
        weights = self.model.cpu().state_dict()
        return weights

    def sendreceiveweights(self, init, weights):
        #For REQ-REP send the first message here
        if not init:
            #TODO send a control message instead of weights to indicate start of transmission
            receiver.send(weights)

        socks = dict(poller.poll())

        if receiver in socks:
            #Check for ACK 
            message = receiver.recv()
            print (message)

        if subscriber in socks:
            #get model params from the server and load them into the local model here.
            message = subscriber.recv()
            message = message[2:]
            #print (message)
            params = json.loads(message)
            for k in params: 
                params[k] = torch.tensor(params[k])
                #print (k) 
            print("RECEIVED WEIGHTS......................................")
            #print(params['fc1.weight'][0])
            self.model.load_state_dict(params)
            receiver.send(weights)

def train():
    train_actor = MNISTTrainActor()
    step = 0
    init = False
    try:
        while True:
            print("Starting training loop # %d. Use Ctrl-C to exit." %(step))
            weights = train_actor.run_train()
            #weights = train_actor.get_weights() 
            print("SENT WEIGHTS......................................")
            #print (weights['fc1.weight'][0])
            for w in weights:
                weights[w] = weights[w].tolist()
            weights = json.dumps(weights)
            step += 1
            if step % 1 == 0:
                train_actor.run_test()
                train_actor.sendreceiveweights(init, weights)
                init = True
    except KeyboardInterrupt:
        print("\nExiting training loop.")

if __name__ == "__main__":
    train()
