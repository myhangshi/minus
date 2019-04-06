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


class Model(nn.Module):
    name = "cifar10"

    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.log_softmax(x, dim=1)


    def __hash__(self):
        return hash(tuple((k, *v.shape) for k, v in self.state_dict().items()))

    #decide whether a data item with idx should be included 
    def data_not_included(self, client_id, idx, target): 
        return (int(client_id[-3:]) % 2) == (idx % 2) 
        #return ((int(client_id[-3:]) % 2)) == (int(target[0]) % 2) 

    def worker_train(self, model=None, args=None, device='cpu', train_loader=None, 
                    epoch=1, client_id='worker100'):

        if model is None: 
            return 

        if train_loader is None: 
            return 

        optimizer = optim.SGD(model.parameters(), lr=args.lr) # TODO momentum is not supported at the moment
        model.train()
    
        loss_history = []
        # need to handle more batches, FIXME 
        # add another loop for epoch here 
        # for each epoch we reort a loss instead 
        for batch_idx, (data, target) in enumerate(train_loader):
            
            if self.data_not_included(client_id, batch_idx, target):
                continue 

            optimizer.zero_grad()
            output = model(data)
        
            loss = F.nll_loss(output, target)
            loss.backward()
            optimizer.step()
        
            if batch_idx % args.log_interval == 0 or batch_idx % args.log_interval == 1:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(train_loader.dataset),
                    100. * batch_idx / len(train_loader), loss.item()))
        
        loss_history.append(loss.item())
        
        return loss_history 


    def worker_test(self, model=None, args=None, device='cpu', test_loader=None, 
                    epoch=1, client_id='worker'):
        if model is None: 
            return 

        model.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in test_loader:
                #data, target = data.to(device), target.to(device)
                output = model(data)
                
                test_loss += F.nll_loss(output, target, reduction='sum').item() # sum up batch loss
                pred = output.argmax(1, keepdim=True) # get the index of the max log-probability 
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
        self.no_cuda = True
        self.seed = 1
        self.log_interval = 200
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


train_loader = torch.utils.data.DataLoader(
    datasets.CIFAR10('./data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                   ])),   
    batch_size=args.batch_size, shuffle=True, **kwargs)

test_loader = torch.utils.data.DataLoader(
    datasets.CIFAR10('./data', train=False, transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                   ])),
    batch_size=args.test_batch_size, shuffle=True, **kwargs)


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
    # unit test from here 
    # 
    '''

    #unit test 1
    model = Model()   

    for epoch in range(1, args.epochs + 1):
        model.worker_train(model, args,  device, train_loader, epoch)
        model.worker_test(model, args,  device, test_loader)


    if (args.save_model):
        torch.save(model.state_dict(), "cifar10_cnn.pt")


    exit() 
    '''
    
    # real work from here 

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
        manager.register_experiment(model, name='cifar10')
        web.run_app(app, port=port)


    elif role == 'worker':
        print('get into worker')
        model = Model()
        worker = LinearTestWorker(app, model, host, port=port, 
            name='cifar10', train_loader=train_loader, test_loader=test_loader, 
            args=args)
        web.run_app(app, port=port)
    
    #while True: 
    #    print("awake, 10 seconds now, sleep again")
    #    time.sleep(10)    
