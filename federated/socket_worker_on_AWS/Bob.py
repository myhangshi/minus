
# coding: utf-8

# # Training the Boston Housing Dataset using PySyft and SocketWorker
# 
# This tutorial is a 3 notebook tutorial. The partners notebooks are the notebooks entitled `SocketWorker Boston Housing Client.ipynb` and `SocketWorker Server Alice.ipynb`. They are in the same folder as this notebook. You should execute this notebook **BEFORE** `SocketWorker Boston Housing Client.ipynb`.
# 

# # Step 1: Hook PyTorch
# 
# Just like previous tutorials, the first step is to override PyTorch commands using the TorchHook object.


import syft as sy

hook = sy.TorchHook(verbose=False)
me = hook.local_worker
me.is_client_worker = False


# # Step 2: Launch Server
# 
# The next step is to launch the server. We set is_pointer=False to tell the worker that this worker object is not merely a connection to a foreign worker but is in fact responsible for computation itself. We set is_client_worker=False to tell the worker to store tensors locally (as opposed to letting a client manage tensor lifecycles).


local_worker = sy.SocketWorker(hook=hook,
                            id='bob',
			    hostname="100.65.100.179",
                            port=2005,
                            is_client_worker=False)



local_worker.listen()

