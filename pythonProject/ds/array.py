import array as arr

a=arr.array('i',[1,2,3,4,5])
a.append(6)
a.pop()
a.insert(1,20)
a.remove(20)
a.reverse()
for i in range(0,len(a)):
    print(a[i])
print(a.index(5))

b=arr.array('f',[1.2,33.33,3.0,2.1233])
for i in range(0,4):
    print(b[i])
ls=[3,4,4,5,6,67,77,88,788,7,7,6]
c=arr.array('i',ls)
for i in range(len(ls)):
    print(c[i])