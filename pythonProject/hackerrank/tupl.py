import builtins
tup=()
N=int(input())
tup=tuple(int(num) for num in input().split())[:N]
k=builtins.hash(tup)


print(k)