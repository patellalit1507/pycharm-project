m=int(input())
A=list(int(num) for num in input().split())[:m]
a=set(A)
n=int(input())
B=list(int(num) for num in input().split())[:n]
b=set(B)
k=a.difference(b)
b=b.difference(a)
k.update(b)
print(k)
