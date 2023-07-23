import array as arr
def search(a,l,s):
    for i in range(l):
        for j in range(i,l):
            if(a[i]+a[j]==s):
                return True
                exit()
    return False


ls=list(int(n) for n in input().split())
s=int(input("enter the digit  "))

a=arr.array('i',ls)
l=len(a)
x=search(a,l,s)
print(x)
