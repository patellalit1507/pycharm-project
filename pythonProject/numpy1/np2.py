import numpy as np
b=np.array([[1,2,3],[3,4,5]],dtype=float)#array using list and deciding dtype
print(' ')
print(b)
a=np.array((1,2,3))
print(a)
print(' ')
c=np.zeros((3,4))#array using zeros
print(c)
print(" ")

d=np.full((3,3),6,dtype=complex)
print(d)
print("")

e=np.random.random((2,2))
print(e)
print(" ")
f=np.arange(0,35,5)
print(f)
print("")
g=np.linspace(0,5,10)
print(g)
print()
h=np.array([[1,2,3,4],[4,5,6,7],[3,5,6,8]])
print(h)
newarr=h.reshape(2,2,3)
print(newarr)