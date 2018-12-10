import syft as sy
import copy
hook = sy.TorchHook()
import torch
from torch import nn, optim
from torchvision import datasets, transforms
import torch.nn.functional as F
import argparse

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
pytorch_total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print("pytorch_total_params ", pytorch_total_params)

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

# create a couple workers

bob = sy.VirtualWorker(id="bob")
alice = sy.VirtualWorker(id="alice")
secure_worker = sy.VirtualWorker(id="secure_worker")

#bob.add_workers([alice, secure_worker])
#alice.add_workers([bob, secure_worker])
#secure_worker.add_workers([alice, bob])

train_distributed_dataset  = []
for batch_idx, (data,target) in enumerate(train_loader):
    if batch_idx > 4: break
    data = sy.Var(data)
    target = sy.Var(target.long())
    data.send(bob)
    target.send(bob)
    train_distributed_dataset.append((data, target))

#bobs_model = model.copy().send(bob)
#alices_model = model.copy().send(alice)

bobs_model = Net()

bobs_opt = optim.SGD(params=bobs_model.parameters(),lr=0.1)
#alices_opt = optim.SGD(params=alices_model.parameters(),lr=0.1)

bobs_model = bobs_model.send(bob)

for p in bobs_model.parameters():
    #print(p.get().shape, p.id, p.id_at_location)
    print(p.get().shape, p.id)

#for i in range(10):
for batch_idx, (data,target) in enumerate(train_distributed_dataset):

    print(data)
    #bobs_model.send(data.location)
    # Train Bob's Model
    bobs_opt.zero_grad() # this is where it breaks.........
    bobs_pred = bobs_model(data)
    bobs_loss = F.nll_loss(bobs_pred, target)
    bobs_loss.backward()

    bobs_opt.step()
    bobs_loss = bobs_loss.get().data[0]
