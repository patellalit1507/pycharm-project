# arr=[0]*5
# print(arr)
#
# arr=[[0 for i in range(5)]for j in range(5)]
# arr[0][0]=1
# for i in arr:
#     print(i)

rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0]=1
for i in arr:
    print(i)