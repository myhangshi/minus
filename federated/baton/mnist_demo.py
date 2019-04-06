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
    name = "lineartest"


    def __init__(self):
        super(Model, self).__init__()
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

    def __hash__(self):
        return hash(tuple((k, *v.shape) for k, v in self.state_dict().items()))

    #decide whether a data item with idx should be included 
    def data_not_included(self, client_id, idx, target): 
        return (int(client_id[-3:]) % 2) == (idx % 2) 
        #return ((int(client_id[-3:]) % 2)) == (int(target[0]) % 2) 

    def worker_train(self, model=None, args=None, device='cpu', train_loader=None, 
                    epoch=1, client_id='worker'):

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
        
            if batch_idx % args.log_interval == 0:
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
        #self.batch_size = 64
        self.batch_size = 32
        self.test_batch_size = 1000
        self.epochs = 10
        self.lr = 0.01
        self.momentum = 0.5
        self.no_cuda = False
        self.seed = 1
        self.log_interval = 2000
        self.save_model = False


def test_merge(): 
    #{k: (sum(all_clients[c][k] for c in all_clients) / len(all_clients)) 
    #                          for k in all_clients[0]  }
        
    #self.model.load_state_dict(mean_params) 

    model1 = Model()   
    for epoch in range(1,  2):
        model1.worker_train(model1, args,  device, train_loader, epoch)
        model1.worker_test(model1, args, device, test_loader)


    model2 = Model()   
    for epoch in range(1,  3):
        model2.worker_train(model2, args, device, train_loader, epoch)
        model2.worker_test(model2, args,  device, test_loader)

    all_clients = {}
    all_clients['c1'] = model1.state_dict()
    all_clients['c2'] = model2.state_dict()

    print(all_clients)
    print("++++++   one more line    ++++++")
    print(all_clients[next(iter(all_clients))])
    print("++++++   one more line    ++++++")

    for c in all_clients: 
        print(c)
    
    print("++++++   one more line    ++++++")
    print("++++++   one more line    ++++++")
    print("++++++   one more line    ++++++")    
    

    model_all = { k: (sum(all_clients[c][k] for c in all_clients) / len(all_clients))
                              for k in all_clients[next(iter(all_clients))]  }
    

    print(model_all)
    print("++++++   end all lines    ++++++") 
    model1.load_state_dict(model_all)

    #torch.save(model_all.state_dict(), "mnist_cnn.pt")

    return model1.state_dict() 



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
    test_merge()
    exit() 

    #unit test 2 
    model = Model()   

    for epoch in range(1, args.epochs + 1):
        model.worker_train(model, args,  device, train_loader, epoch)
        model.worker_test(model, args,  device, test_loader)


    #for epoch in range(1, args.epochs + 1):
    #    train(model, args,  device, train_loader, optimizer, epoch)
    #    test(model, args,  device, test_loader)

    if (args.save_model):
        torch.save(model.state_dict(), "mnist_cnn.pt")


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
        manager.register_experiment(model, name='linear')
        web.run_app(app, port=port)


    elif role == 'worker':
        print('get into worker')
        model = Model()
        worker = LinearTestWorker(app, model, host, port=port, 
            name='linear', train_loader=train_loader, test_loader=test_loader, 
            args=args)
        web.run_app(app, port=port)
    
    #while True: 
    #    print("awake, 10 seconds now, sleep again")
    #    time.sleep(10)    
