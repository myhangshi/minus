
# coding: utf-8

# # Training the Boston Housing Dataset using PySyft and SocketWorker
# 
# This tutorial is a 3 notebook tutorial. The partners notebooks are the notebooks entitled `SocketWorker Server Alice.ipynb` and `SocketWorker Server Bob.ipynb`. They are in the same folder as this notebook. You should execute this notebook **AFTER** you have executed the others.
# 
# This tutorial is an example of training a neural network in a federated fashion on the Boston Housing dataset using socketworkers, python instances Alice and Bob running in the two other tabs you have opened in your browser.
# 
# Before starting with this notebook, we recommend looking at `toy/Federated Learning Example.ipynb` which provides a basic example.
# 
# Preformance: achieves ~20 MSE in 10 epochs in 25s _(Perf. measured on [colab.research.google.com/17upxC...](https://colab.research.google.com/drive/17upxCYJmJ6Zoxv0KjiJ1ZbchlJybsfhs))_
# 
# _This notebook doesn't intend to provide a good prediction model and rather focuses on computation overhead due to federated learning._
# 
# The base example without federated learning can be found here: [colab.research.google.com/drive/1ne4ra...](https://colab.research.google.com/drive/1ne4rap-8nD6-jABV94fkPBHvtPj-RrKY#scrollTo=i_gUp-uFfwGL)
# 
# 

# # Setting Up

# In[1]:


from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader
# from keras.datasets import boston_housing

print(torch.__version__)
# Training settings
parser = argparse.ArgumentParser(description='PyTorch Example')
parser.add_argument('--batch-size', type=int, default=8, metavar='N',
                    help='input batch size for training (default: 8)')
parser.add_argument('--test-batch-size', type=int, default=8, metavar='N',
                    help='input batch size for testing (default: 8)')
parser.add_argument('--epochs', type=int, default=10, metavar='N',
                    help='number of epochs to train (default: 10)')
parser.add_argument('--lr', type=float, default=0.001, metavar='LR',
                    help='learning rate (default: 0.001)')
parser.add_argument('--momentum', type=float, default=0.0, metavar='M',
                    help='SGD momentum (default: 0.0)')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                    help='how many batches to wait before logging training status')
args = parser.parse_args([])


torch.manual_seed(args.seed)
kwargs = {}


# ### Loading the dataset

# In[2]:


import pickle
f = open('../other/data/boston_housing.pickle','rb')
((X, y), (X_test, y_test)) = pickle.load(f)
f.close()


# In[3]:




X = torch.from_numpy(X).type(torch.FloatTensor)
y = torch.from_numpy(y).type(torch.FloatTensor)
X_test = torch.from_numpy(X_test).type(torch.FloatTensor)
y_test = torch.from_numpy(y_test).type(torch.FloatTensor)
# preprocessing
mean = X.mean(0, keepdim=True)
dev = X.std(0, keepdim=True)
mean[:, 3] = 0. # the feature at column 3 is binary,
dev[:, 3] = 1.  # so I'd rather not standardize it
X = (X - mean) / dev
X_test = (X_test - mean) / dev
train = TensorDataset(X, y)
test = TensorDataset(X_test, y_test)
train_loader = DataLoader(train, batch_size=args.batch_size, shuffle=True, **kwargs)
test_loader = DataLoader(test, batch_size=args.test_batch_size, shuffle=True, **kwargs)


# #  Neural Network Structure

# In[4]:


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(13, 32)
        self.fc2 = nn.Linear(32, 24)
        self.fc3 = nn.Linear(24, 1)

    def forward(self, x):
        x = x.view(-1, 13)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = Net()


optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum)


# # Hooking into Pytorch

# In[5]:


import syft
import syft as sy
from syft.core import utils
import torch
import torch.nn.functional as F
import json
import random
from syft.core.frameworks.torch import utils as torch_utils
from torch.autograd import Variable

local_worker = sy.SocketWorker(id="local", port=2009, hook=None, is_client_worker=False)
hook = sy.TorchHook(local_worker=local_worker, verbose=False)
me = hook.local_worker
me.hook = hook



# In[6]:

alice = sy.SocketWorker(id="alice", hostname="54.173.218.212", port=2006, hook=hook, is_pointer=True, is_client_worker=False)
#alice = sy.SocketWorker(id="alice", hostname="172.31.33.80", port=2006, hook=hook, is_pointer=True, is_client_worker=False)

bob = sy.SocketWorker(id="bob", hostname="18.208.151.226", port=2005, hook=hook, is_pointer=True, is_client_worker=False)

compute_nodes = [bob, alice]

me.add_workers([bob, alice])
#bob.add_workers([me, alice])
#alice.add_workers([me, bob])


# **Send data to the worker** <br>
# Usually they would already have it, this is just for demo

# In[7]:


train_distributed_dataset = []

for batch_idx, (data,target) in enumerate(train_loader):
    print(batch_idx)
    data = Variable(data)
    target = Variable(target.float())
    data.send(compute_nodes[batch_idx % len(compute_nodes)])
    target.send(compute_nodes[batch_idx % len(compute_nodes)])
    train_distributed_dataset.append((data, target))


# # Training Function

# In[8]:


def train(epoch):
    model.train()
    for batch_idx, (data,target) in enumerate(train_distributed_dataset):
            
        worker = data.location
        model.send(worker)

        optimizer.zero_grad()
        # update the model
        pred = model(data)
        loss = F.mse_loss(pred, target.float())
        loss.backward()
        model.get()
        optimizer.step()

        if batch_idx % args.log_interval == 0:
            loss.get()
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * args.batch_size, len(train_loader) * args.batch_size,
                100. * batch_idx / len(train_loader), loss.data[0]))
        


# # Testing Function

# In[9]:


def test():
    model.eval()
    test_loss = 0
    for data, target in test_loader:

        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data)
        test_loss += F.mse_loss(output, target.float(), size_average=False).data[0] # sum up batch loss
        pred = output.data.max(1, keepdim=True)[1] # get the index of the max log-probability
        
    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}\n'.format(test_loss))


# # Training The Dataset

# In[10]:


#get_ipython().run_cell_magic('time', '', '\nfor epoch in range(1, args.epochs + 1):\n    train(epoch)')


# # Calculating Performance

# In[11]:


test()

