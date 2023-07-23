import operator

li=[1,3,4,5,5,6,6,str]

for i in range(0, len(li)):
    print(li[i],end=",")
print("\r")

operator.setitem(li,3,23)

for i in range(0, len(li)):
    print(li[i],end=",")
print("\r")