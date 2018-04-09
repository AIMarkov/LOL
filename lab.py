import torch.nn as nn
import torch
from torch.autograd import Variable

loss=nn.CrossEntropyLoss(reduce=False)
input=Variable(torch.randn(3,5),requires_grad=True)
target=Variable(torch.LongTensor(3).random_(5))
a=Variable(torch.Tensor([1,2,1]))
output=torch.mean(loss(input,target)*a ) #torch.matmul(loss(input,target),a)
print(loss(input,target)*a )
print(output)
output.backward()
print(output)
