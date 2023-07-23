import array as arr
import numpy as np
def cal(arr):
    sum=[]
    for i in range(4):
        for j in range(4):
            s1=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            s2=arr[i+1][j+1]
            s3=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            temp=s1+s2+s3
            sum.append(temp)
    return max(sum)
a=[]
for i in range(6):
    a.append(list(map(int,input().split())))
print(cal(a))
