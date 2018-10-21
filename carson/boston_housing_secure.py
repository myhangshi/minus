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
model_params = list(model.parameters())

bobs_model = Net()
alices_model = Net()

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

me.add_workers([bob, alice])
bob.add_workers([me, alice])
alice.add_workers([me, bob])

remote_dataset = (list(),list())

for batch_idx, (data,target) in enumerate(train_loader):
    data = Variable(data)
    target = Variable(target.float())
    data.send(compute_nodes[batch_idx % len(compute_nodes)])
    target.send(compute_nodes[batch_idx % len(compute_nodes)])
    remote_dataset[batch_idx % len(compute_nodes)].append((data, target))


def update(data, target, model, optimizer):
    model.send(data.location)
    optimizer.zero_grad()
    pred = model(data)
    loss = F.mse_loss(pred, target.float())
    loss.backward()
    bobs_optimizer.step()
    return model

bobs_optimizer = optim.SGD(bobs_model.parameters(), lr=args.lr, momentum=args.momentum)
alices_optimizer = optim.SGD(alices_model.parameters(), lr=args.lr, momentum=args.momentum)

models = [bobs_model, alices_model]
params = [list(bobs_model.parameters()), list(alices_model.parameters())]
optimizers = [bobs_optimizer, alices_optimizer]

def train():

    for data_index in range(len(remote_dataset[0])-1):
        # update remote models
        for remote_index in range(len(compute_nodes)):
            data, target = remote_dataset[remote_index][data_index]
            models[remote_index] = update(data, target, models[remote_index], optimizers[remote_index])

        new_params = list()

        for param_i in range(len(params[0])):

            spdz_params = list()
            for remote_index in range(len(compute_nodes)):
                spdz_params.append((params[remote_index][param_i].data+0).fix_precision().share(bob, alice).get())

            new_param = (spdz_params[0] + spdz_params[1]).get().decode()/2
            new_params.append(new_param)

        for model in params:
            for param in model:
                param.data *= 0

        for model in models:
            model.get()

        for remote_index in range(len(compute_nodes)):
            for param_index in range(len(params[remote_index])):
                params[remote_index][param_index].data.set_(new_params[param_index])


def test():
    models[0].eval()
    test_loss = 0
    for data, target in test_loader:
        data, target = Variable(data, volatile=True), Variable(target)
        output = models[0](data)
        test_loss += F.mse_loss(output, target.float(), size_average=False).data[0] # sum up batch loss
        pred = output.data.max(1, keepdim=True)[1] # get the index of the max log-probability
        
    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}\n'.format(test_loss))

for epoch in range(1, args.epochs + 1):
    print(epoch)
    train()
    test()


# import tensorflow as tf
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


