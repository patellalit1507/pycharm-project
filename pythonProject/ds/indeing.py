arr=[]
arr=list(int(N) for N in input().split())
value=int(input("entr the value"))
arr.sort()
print(arr)
n=len(arr)
lo=0
hi=n-1

while(lo<=hi) :
    mid=int((lo+hi)/2)
    #print(mid)
    if arr[mid]==value:
        print("value found at index: ",mid)
        break
    elif arr[mid]<value:
        lo=mid+1
    elif arr[mid]>value:
        hi=mid-1

