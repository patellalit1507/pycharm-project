import time
import math

def calculatetime_fun(func):
    def inner1(*args,**kwargs):
        begin=time.time()
        func(*args,**kwargs)
        end=time.time()
        print("total time taken_",func.__name__,end-begin)
    return inner1

#@calculatetime_fun
#def factorial(num):
#   time.sleep(3)
#   print(math.factorial(num))

def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial=calculatetime_fun(factorial)



factorial(10)