from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader

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


import pickle
f = open('./other/data/boston_housing.pickle','rb')
((X, y), (X_test, y_test)) = pickle.load(f)
f.close()

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

import syft
import syft as sy
from syft.core import utils
import torch
import torch.nn.functional as F
import json
import random
from syft.core.frameworks.torch import utils as torch_utils
from torch.autograd import Variable
hook = sy.TorchHook(verbose=False)
me = hook.local_worker
bob = sy.VirtualWorker(id="bob",hook=hook, is_client_worker=False)
alice = sy.VirtualWorker(id="alice",hook=hook, is_client_worker=False)
me.is_client_worker = False

compute_nodes = [bob, alice]

bob.add_workers([alice])
alice.add_workers([bob])

train_distributed_dataset = []

for batch_idx, (data,target) in enumerate(train_loader):
    data = Variable(data)
    target = Variable(target.float())
    data.send(compute_nodes[batch_idx % len(compute_nodes)])
    target.send(compute_nodes[batch_idx % len(compute_nodes)])
    train_distributed_dataset.append((data, target))


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


import time


t = time.time()
args.epochs = 10
torch.encode_timer = 0
torch.handle_call_timer = 0
torch.execute_call_timer = 0

for epoch in range(1, args.epochs + 1):
    train(epoch)

    
total_time = time.time() - t
print('Encoding', round(torch.encode_timer, 2), 's', round(torch.encode_timer/total_time*100, 2), '%')
print('Handling', round(torch.handle_call_timer, 2), 's',  round(torch.handle_call_timer/total_time*100, 2), '%')
print('Execute call', round(torch.execute_call_timer, 2), 's',  round(torch.execute_call_timer/total_time*100, 2), '%')
print('Total', round(total_time, 2), 's')



