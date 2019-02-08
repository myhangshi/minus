import copy
import torch
from torch import nn, optim
from torchvision import datasets, transforms
import torch.nn.functional as F
from torch.autograd import Variable

from syft import optim



import argparse
import syft as sy


train_dataset  = datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ]))


test_dataset  = datasets.MNIST('../data', train=False, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ]))


print("training data len and target len ", len(train_dataset.train_data),  
                                            len(train_dataset.train_labels))

print("test data len and target len ", len(test_dataset.test_data),  
                                       len(test_dataset.test_labels))


 

hook = sy.TorchHook(torch)
me = hook.local_worker
#me.is_client_worker = False

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
#args.cuda = not args.no_cuda and torch.cuda.is_available()
args.cuda = False 

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        print("x size is ", x.shape)
        

        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


model = Net()
bobs_model = Net()

bobs_opt = optim.SGD(params=bobs_model.parameters(),lr=0.1)


#alices_opt = optim.SGD(params=alices_model.parameters(),lr=0.1)

pytorch_total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print("pytorch_total_params ", pytorch_total_params)

#kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}
kwargs = {}



#self.data, self.targets = torch.load(os.path.join(self.processed_folder, data_file))


#train_loader = torch.utils.data.DataLoader(
#    datasets.MNIST('../data', train=True, download=True,
#                   transform=transforms.Compose([
#                       transforms.ToTensor(),
#                       transforms.Normalize((0.1307,), (0.3081,))
#                   ])),
#    batch_size=args.batch_size, shuffle=True, **kwargs)



#train_loader = torch.utils.data.DataLoader(
#    datasets.MNIST('../data', train=True, download=True,
#                   transform=transforms.Compose([
#                       transforms.ToTensor(),
#                       transforms.Normalize((0.1307,), (0.3081,))
#                   ])),
#    batch_size=args.batch_size, shuffle=True, **kwargs)

#test_loader = torch.utils.data.DataLoader(
#    datasets.MNIST('../data', train=False, transform=transforms.Compose([
#                       transforms.ToTensor(),
#                       transforms.Normalize((0.1307,), (0.3081,))
#                   ])),
#    batch_size=args.test_batch_size, shuffle=True, **kwargs)

#print("len is ", len(train_loader)) 
#print("len is ", len(test_loader)) 

# create a couple workers

#bob = sy.VirtualWorker(id="bob", hook=hook)
#alice = sy.VirtualWorker(id="alice",hook=hook)
#secure_worker = sy.VirtualWorker(id="secure_worker",hook=hook)

bob = sy.VirtualWorker(id="bob",hook=hook, is_client_worker=False)
#alice = sy.VirtualWorker(id="alice",hook=hook, is_client_worker=False)


me.add_worker(bob)
#me.add_worker(alice)

#bobs_model = model.copy().send(bob)
#alices_model = model.copy().send(alice)

#bob.add_workers([alice, secure_worker])
#alice.add_workers([bob, secure_worker])
#secure_worker.add_workers([alice, bob])

train_distributed_dataset  = []


for batch_idx, (dk,target) in enumerate(train_dataset):
    #print("data set ", batch_idx, data, target)
    #if batch_idx 
    if batch_idx % 2000 == 1999: 
        print("data set ", batch_idx, dk.shape, target.shape)
    #data = torch.Tensor(data)
    #target = torch.Tensor(target
    if batch_idx == 6000: 
        break 


    data = torch.from_numpy(dk.unsqueeze(0).numpy())


    #target = Variable(target.unsqueeze(0))

    if batch_idx % 2000 == 1999: 
        print("data set new ", batch_idx, data.shape, target.shape)
    

    data.send(bob)
    target.send(bob)
    train_distributed_dataset.append((data, target))

print("the length is ", len(train_distributed_dataset))


#exit 


bobs_model = bobs_model.send(bob)

#for p in bobs_model.parameters():
#	print(p.get().shape, p.id, p.id_at_location)
#    print(p.get().shape, p.id)

#for i in range(10):
bobs_model.train() 

for batch_idx, (data,target) in enumerate(train_distributed_dataset):

    #print(data)
    #bobs_model.send(data.location)
    # Train Bob's Model
    bobs_opt.zero_grad() # this is where it breaks.........
    bobs_pred = bobs_model(data)
    print("debugging dim here is ", bobs_pred.shape, target.shape)
    bobs_loss = F.nll_loss(bobs_pred, target)
    
    bobs_opt.step()
    bobs_loss = bobs_loss.get()
    
    bobs_loss.backward()

    if batch_idx % 1000 == 999:
        print("the loss now is %f ", bobs_loss.data[0])



