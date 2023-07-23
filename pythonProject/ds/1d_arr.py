# n=int(input())
# ar=[0]*n
# print(ar)
# this is 1st way to create arr

# n=int(input())
# arr=[0 for i in range(n)]
# print(arr)

rows,cols=(5,5)
arr=[[0]*rows]*cols
arr[0][0]=1
for row in arr:
    print(row)
# 1st way to create 2d array

# now 2nd way is
# rows,cols=(5,5)
# arr=[[0 for i in range(cols)] for j in range(rows)]
# # arr=[0 for i in range(cols)]*rows  that is not true
# arr[0][0]=1
# for row in arr:
#     print(row)