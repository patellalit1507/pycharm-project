def permutation(a, l, r):
    if l==r:
        print("".join(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permutation(a,l+1,r)
            a[l],a[i]=a[i],a[l]

if __name__ == '__main__':
    s=list(input())
    permutation(s,0,len(s)-1)