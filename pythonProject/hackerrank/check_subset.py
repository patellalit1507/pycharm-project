
n=int(input())
out=[]
def getList(n):
    temp=list(int(num) for num in input().split())[:n]
    return temp
for i in range(n):
    a=[]
    b=[]
    na=int(input())
    a=getList(na)
    nb=int(input())
    b=getList(nb)
    if (set(a).issubset(set(b))):
        out.append(True)
    else:
        out.append(False)

for i in range(n):
    print(out[i])