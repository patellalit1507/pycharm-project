def swap(start,end,ele):
    ele[start],ele[end]=ele[end],ele[start]
def partition(start,end,ele):
    pivot_index=start
    pivot_vlaue=ele[pivot_index]
    #start=pivot_index+1
    #end=len(ele)-1
    while start<end:
       while start<len(ele) and ele[start]<=pivot_vlaue:
            start=start+1

       if end<=0:
        while ele[end]>=pivot_vlaue:
            end-=1



       if start<end:
          swap(start,end,ele)

    swap(pivot_index,end,ele)
    return end







def quick_sort(start,end,ele):
     if start<end:
       k= partition(start,end,ele)
       quick_sort(start,k-1,ele)
       quick_sort(k+1,end,ele)




if __name__ == '__main__':
    ele=[11,9,7,12,5,23,29,7,2,15,28]
    quick_sort(0,len(ele)-1,ele)
    print(ele)
