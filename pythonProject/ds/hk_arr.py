n=int(input())
arr=list(int(num) for num in input().split())[:n]
stack=[]
temp=n
for i in reversed(arr):
    print(i,end=" ")
