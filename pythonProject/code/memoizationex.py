#def facto(numm):
#    if numm==1:
#        return 1
#    else:
#        return numm*facto(numm-1)
#print(facto(10))
#this above fun is for finding factorial without using memonization
def memo_num(func):
    memory={}
    def inner(num):
        if num not in memory:
            print('g')
            memory[num]=func(num)
        return memory[num]
    return inner


@memo_num
def facto(numm):
   if numm==1:
        return 1
   else:
       return numm*facto(numm-1)
print(facto(10))