n=str(input())
li=[]
f=[]
c=0
t=1
l=len(n)
if(l%2==0):
   for i in range(0,int(l/2)):
         li.append(n[c:c+2])
         c=c+2
else:
   for i in range(0,int(l/2)+1):
       li.append(n[c:c + 2])
       c = c + 2
for i in li:
    if t%2==0:
        f.append(i[0])
        t=t+1
    else:
        try:
            f.append(i[1])
        except:
            f.append(i[0])
        t=t+1

for i in f:
    print(i,end="")