from util import time_it
@time_it
def linear_serch(list,find):
    for inde,ele in enumerate(list):
        if ele==find:
            return inde
    return -1
@time_it
def binary_search(list,find):
    left_index=0
    right_index=len(list)-1
    mid_index=0


    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=list[mid_index]

        if mid_number==find:
            return mid_index
        if mid_number<find:
            left_index=mid_index+1

        if mid_number>find:
            right_index=mid_index-1
    return -1



if __name__ == '__main__':
    #list=[1,2,3,4,4,5,6,7,8,34,23,4,56,6,7,4,322,445,67,7,55,334]
    #list.sort()
    list=[i for i in range(100000001)]
    find=100000000
    print(binary_search(list,find))
    print(linear_serch(list,find))

