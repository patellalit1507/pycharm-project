from util import time_it
import random
@time_it
def Bubble_sort(list):
    l=len(list)
    for j in range(l-1):
     for i in range(l-1-j):
         #swap=False
         if list[i]>list[i+1]:
             temp=list[i+1]
             list[i+1]=list[i]
             list[i]=temp
             #swap=True


    return list



if __name__ == '__main__':
    list=[]
    for i in range(1000):
        list.append(random.randint(1,10000))


    print(Bubble_sort(list))


