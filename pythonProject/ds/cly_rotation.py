import array as arr
def rotate_arr(a,l):
    temp_arr=a[l-1]
    a.remove(a[l-1])
    a.insert(0,temp_arr)
    return a

k=list(int(n) for n in input("enter the elements of arr ").split())
a=arr.array("i",k)
l=len(a)
cly=rotate_arr(a,l)
for i in range(l):
    print(cly[i],end=' ')