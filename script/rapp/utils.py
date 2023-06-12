import torch
import numpy as np 

def torch2np(x_torch):
    return x_torch.detach().cpu().numpy()
def np2torch(x_np,device='cpu'):
    return torch.tensor(x_np,dtype=torch.float32,device=device)
print ("Done.")