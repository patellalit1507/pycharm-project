import array as arr
ls=list(map(int,input().split()))
n=len(ls)

for j in range(1,n):
    key=ls[j]
    i=j-1
    while i>-1 and ls[i]>key:
        ls[i+1]=ls[i]
        i=i-1
    ls[i+1]=key

print(ls)

