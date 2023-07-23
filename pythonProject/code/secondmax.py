
N=int(input())
l=list(int(num) for num in input().strip().split())[:N]
l.sort()

for i in reversed(l):
  if(l[N-1]>i):
    print(i)
    break