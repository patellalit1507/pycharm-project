# Input: An integer money and an array of d denominations c =
# (c1; c2; : : : ; cd), in decreasing order of value (c1 > c2 >    > cd).
# Output: A list of d integers i1; i2; : : : ; id such that c1  i1 + c2  i2 +
#    + cd  id = money; and i1 + i2 +    + id is as small as possible.

import array as arr
def count(m,a):
    ls=[]
    temp=int(m)
    for i in a:
        ls.append(int(temp/i))
        temp=temp%(int(i))
    return ls

# brut force approach
def brutforcechange(m:int,a):
    dp=[m+1]*(m+1)
    dp[0]=0
    for i in range(1,m+1):
          for c in a:
              if i-c>=0:
                  dp[i]=min(dp[i],1+dp[i-c])
    return dp[m] if dp[m]!=1+m else -1
if __name__ == '__main__':
    money=int(input())
    ls=list(map(int,input().split()))
    k=brutforcechange(money,ls)
    print(k)
