from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

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
args = parser.parse_args([])
args.cuda = not args.no_cuda and torch.cuda.is_available()

torch.manual_seed(args.seed)
if args.cuda:
    torch.cuda.manual_seed(args.seed)


kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}
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

dataset_train = datasets.MNIST('../data/', train=True, download=True,
                       transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                ]))
    
#print (len(dataset_train))
#print (dataset_train.train_labels)

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

model = Net()
if args.cuda:
    model.cuda()



bobs_optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum)
alice_optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum)


optimizers = [bobs_optimizer,  alice_optimizer]


#from syft.core.hooks import TorchHook
#from syft.core.workers import VirtualWorker
import torch
import torch.nn as nn
from torch.autograd import Variable as Var
import torch.optim as optim

import syft as sy 


# this is our hook
hook = sy.TorchHook()
me = hook.local_worker
me.is_client_worker = False 

bob = sy.VirtualWorker(id='bob',hook=hook, is_client_worker=False)
alice = sy.VirtualWorker(id='alice',hook=hook, is_client_worker=False)

#me.add_workers([bob, alice])
bob.add_workers([alice])
alice.add_workers([bob])

compute_nodes = [bob, alice]
train_distributed_dataset  = []

i = 0
for batch_idx, (data,target) in enumerate(train_loader):
    if batch_idx + 1 % 100 == 0: 
        print(batch_idx)
        break 
    data = Variable(torch.from_numpy(data.numpy()))
    #print (data.shape)
    #target = Variable(target.float())
    target = Variable(target)
    data.send(compute_nodes[batch_idx % len(compute_nodes)])
    target.send(compute_nodes[batch_idx % len(compute_nodes)])
    train_distributed_dataset.append((data, target))
#bobs_optimizer.send(bob)
#alice_optimizer.send(alice)

len_train_loader = len(train_loader.dataset) #needed below for loss and accuracy calculation
#train_loader = None #free memory

def train(epoch):
    model.train()
    print("get into train function ")
    #for batch_idx, (data, target) in enumerate(train_loader):
    for batch_idx, (data,target) in enumerate(train_distributed_dataset):
        worker = data.location
        model.send(worker)

        optimizer = optimizers[batch_idx % len(compute_nodes)]
        #data, target = Variable(data), Variable(target)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        model.get()
        optimizer.step()
        
        
    return 
    
def test():
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data)
        test_loss += F.nll_loss(output, target, size_average=False).data[0] # sum up batch loss
        pred = output.data.max(1, keepdim=True)[1] # get the index of the max log-probability
        correct += pred.eq(target.data.view_as(pred)).long().cpu().sum()

    test_loss /= len_train_loader #len(test_loader.dataset)
    #print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
    #    test_loss, correct, len(test_loader.dataset),
    #    100. * correct / len(test_loader.dataset)))
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len_train_loader,
        100. * correct / len_train_loader))

#for epoch in range(1, args.epochs + 1):
for epoch in range(1, 3):
    train(epoch)
    #test()

