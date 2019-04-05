from __future__ import print_function
import argparse

import torch
from torch import nn
from torch import optim
from torch.nn import functional
import torch.nn.functional as F
from torch import autograd
from torchvision import datasets, transforms
import random
import time 



from aiohttp import web

from utils import EpochProgress
from manager import Manager
from worker import ExperimentWorker


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

def train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        #data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % args.log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

def test(args, model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            #data, target = data.to(device), target.to(device)
            output = model(data)
            #test_loss += F.nll_loss(output, target, reduction='sum').item() # sum up batch loss
            test_loss += F.nll_loss(output, target).item() # sum up batch loss
        #print("test_loss ", test_loss)
        #exit()
            pred = output.max(1, keepdim=True)[1] # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))



class Arguments():
    def __init__(self):
        self.batch_size = 64
        self.test_batch_size = 1000
        self.epochs = 10
        self.lr = 0.01
        self.momentum = 0.5
        self.no_cuda = False
        self.seed = 1
        self.log_interval = 30
        self.save_model = False

args = Arguments()

use_cuda = not args.no_cuda and torch.cuda.is_available()
use_cuda = 0 

torch.manual_seed(args.seed)



device = torch.device("cuda" if use_cuda else "cpu")

kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}


train_loader = torch.utils.data.DataLoader(
        datasets.MNIST('../data', train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])),
        batch_size=args.batch_size, shuffle=True, **kwargs)

test_loader = torch.utils.data.DataLoader(
        datasets.MNIST('../data', train=False, transform=transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])),
        batch_size=args.test_batch_size, shuffle=True, **kwargs)


model = Net().to(device)


optimizer = optim.SGD(model.parameters(), lr=args.lr) # TODO momentum is not supported at the moment

for epoch in range(1, args.epochs + 1):
    train(args, model, device, train_loader, optimizer, epoch)
    test(args, model, device, test_loader)

if (args.save_model):
    torch.save(model.state_dict(), "mnist_cnn.pt")


class Model(nn.Module):
    name = "lineartest"

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 1)

    def forward(self, X):
        X = self.fc1(X)
        return X

    def __hash__(self):
        return hash(tuple((k, *v.shape) for k, v in self.state_dict().items()))

    def train(self, X, y, n_epoch=32, lr=0.001, batch_size=32, verbose=True):
        X = autograd.Variable(X)
        y = autograd.Variable(y)
        loss = nn.MSELoss()
        idxs = torch.randperm(X.shape[0])
        optimizer = optim.SGD(self.parameters(), lr=lr)
        loss_history = []
        for epoch in range(n_epoch):
            batch_iter = EpochProgress(epoch, torch.split(idxs, batch_size),
                                       verbose=verbose)
            for batch_idxs in batch_iter:
                optimizer.zero_grad()
                X_batch = X[batch_idxs]
                y_batch = y[batch_idxs]
                output = self(X_batch)
                loss_batch = loss(output, y_batch)
                batch_iter.update_loss(loss_batch)
                loss_batch.backward()
                optimizer.step()
            loss_history.append(batch_iter.loss)
        return loss_history


class LinearTestWorker(ExperimentWorker):
    def get_data(self):
        print("read data for linearTestWorker ")
        n = random.randint(5, 20)
        p = torch.Tensor((11, 5, 3, 2, 5, 6, 2, 7, 8, 1))
        X = torch.randn(32*n, 10)
        y = (p * X).sum(1)
        print(y.shape)
        return (X, y), n*32


if __name__ == "__main__":

    main() 
    exit() 


    import sys
    role = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    app = web.Application()
    print("role is " + role)

    if role == 'manager':
        #app = web.Application()
        manager = Manager(app)
        model = Model()
        manager.register_experiment(model, name='linear')
        web.run_app(app, port=port)


    elif role == 'worker':
        print('get into worker')
        model = Model()
        worker = LinearTestWorker(app, model, host, port=port, 
                                  name='linear')
        web.run_app(app, port=port)
    
    #while True: 
    #    print("awake, 10 seconds now, sleep again")
    #    time.sleep(10)    
