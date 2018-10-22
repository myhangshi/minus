#!/usr/bin/env python3

from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

import syft 
import syft as sy 



#import tensorflow as tf


print("test loading mnist data ")

ds =  datasets.MNIST('../data', train=True, download=True)


exit() 


args = parser.parse_args([])
args.cuda = not args.no_cuda and torch.cuda.is_available()

torch.manual_seed(args.seed)
if args.cuda:
    torch.cuda.manual_seed(args.seed)


kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}



(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_tain / 255.0, x_test / 255.0


x_train = torch.from_numpy(x_train)
y_train = torch.from_numpy(y_train)
x_test = torch.from_numpy(x_test)
y_test = torch.from_numpy(y_test)

# preprocessing
mean = x_r.mean(0, keepdim=True)
dev = X.std(0, keepdim=True)
x_train = (x_train - mean) / dev
x_test = (x_test - mean) / dev

train = TensorDataset(x_train, y_train)
test = TensorDataset(x_test, y_test)

train_loader = DataLoader(train, batch_size=args.batch_size, shuffle=True, **kwargs)
test_loader = DataLoader(test, batch_size=args.test_batch_size, shuffle=True, **kwargs)



exit() 



#
# main program logic starts 
#

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


