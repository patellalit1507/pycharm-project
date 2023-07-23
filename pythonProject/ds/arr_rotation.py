import array as arr

def rotate(a,d,l):
    ls=[]
    for i in range(d):
        ls.append(a[0])
        a.remove(a[0])
    for i in range(d):
        a.append(ls[i])
    return a


k=list(int(n) for n in input("enter the elements of arr ").split())
a=arr.array("i",k)
l=len(a)
d=int(input("enter no of element to rotate "))
ar=rotate(a,d,l)
for i in range(l):
    print(ar[i])


