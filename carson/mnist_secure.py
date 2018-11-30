from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader

import syft
import syft as sy
from syft.core import utils
import json
import random
from syft.core.frameworks.torch import utils as torch_utils


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



# Training settings
parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                    help='input batch size for training (default: 64)')
parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
                    help='input batch size for testing (default: 1000)')
parser.add_argument('--epochs', type=int, default=10, metavar='N',
                    help='number of epochs to train (default: 10)')
parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                    help='learning rate (default: 0.01)')
parser.add_argument('--momentum', type=float, default=0.5, metavar='M',
                    help='SGD momentum (default: 0.5)')
parser.add_argument('--no-cuda', action='store_true', default=False,
                    help='disables CUDA training')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                    help='how many batches to wait before logging training status')
args = parser.parse_args()
use_cuda = not args.no_cuda and torch.cuda.is_available()

torch.manual_seed(args.seed)

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



def update(data, target, model, optimizer):
    model.send(data.location)
    optimizer.zero_grad()
    output = model(data)
    #loss = F.mse_loss(pred, target.float())
    #loss.backward()
    #bobs_optimizer.step()
    loss = F.nll_loss(output, target)
    loss.backward()
    optimizer.step()
    return model



def my_train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()

    return 


model = Net()
model_params = list(model.parameters())

bobs_model = Net()
alices_model = Net()

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
    #if batch_idx > 20: 
    #    break 
    data = Variable(data)
    target = Variable(target)
    data.send(compute_nodes[batch_idx % len(compute_nodes)])
    target.send(compute_nodes[batch_idx % len(compute_nodes)])
    remote_dataset[batch_idx % len(compute_nodes)].append((data, target))


bobs_optimizer = optim.SGD(bobs_model.parameters(), lr=args.lr, momentum=args.momentum)
alices_optimizer = optim.SGD(alices_model.parameters(), lr=args.lr, momentum=args.momentum)

print("model stuff ")
models = [bobs_model, alices_model]
params = [list(bobs_model.parameters()), list(alices_model.parameters())]
optimizers = [bobs_optimizer, alices_optimizer]

def train():

    for data_index in range(len(remote_dataset[0])-1):
    #for data_index in range(1000):
        for remote_index in range(len(compute_nodes)):
        
            # update remote models
            data, target = remote_dataset[remote_index][data_index]
            models[remote_index] = update(data, target, models[remote_index], optimizers[remote_index])

        #new_params = list()

        #for param_i in range(len(params[0])):

        #    spdz_params = list()
        #    for remote_index in range(len(compute_nodes)):
        #        spdz_params.append((params[remote_index][param_i].data+0).fix_precision().share(bob, alice).get())

        #    new_param = (spdz_params[0] + spdz_params[1]).get().decode()/2
        #    new_params.append(new_param)

        #for model in params:
        #    for param in model:
        #        param.data *= 0

        for model in models:
            model.get()

        #for remote_index in range(len(compute_nodes)):
        #    for param_index in range(len(params[remote_index])):
        #        params[remote_index][param_index].data.set_(new_params[param_index])


def test():
    models[0].eval()
    test_loss = 0
    correct = 0

    for data, target in test_loader:
        data, target = Variable(data, volatile=True), Variable(target)
        output = models[0](data)
        
        test_loss += F.nll_loss(output, target, size_average=False).data[0] # sum up batch loss
        pred = output.data.max(1, keepdim=True)[1] # get the index of the max log-probability
        correct += pred.eq(target.data.view_as(pred)).long().cpu().sum()


    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


    
#for epoch in range(1, args.epochs + 1):
for epoch in range(1, 6):
    print(epoch)
    train()


test()



#if __name__ == '__main__':
#    main()
