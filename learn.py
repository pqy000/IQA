import torch
a=torch.randn(4,3)

b,c = a.split([2,2],dim=0)
print(a.shape[0], a.shape[1])
#把维度0按照长度[1,2]拆分，形成2个tensor，shape（1，4）和 shape（2，4）
print(a)
print(b)
print(c)
# a.split([2,2],dim=1)

a=torch.randn(4,6)
b, c = a.chunk(2,dim=0)
#返回一个shape（2，6）的tensor
print(a)
print(b)
print(c)
a.chunk(2,dim=1)