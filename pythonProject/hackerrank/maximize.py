import math
import sys

n,m=sys.stdin
l=[]
#int(m)

for i in range(int(n)):
    k=list(int(num) for num in input().split())
    l.append(max(k)**2)
print(sum(l)%int(m))
