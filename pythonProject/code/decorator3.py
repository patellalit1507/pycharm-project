def decorator_fun(x,y):
    def inner(func):
        def wrapper(*args,**kwargs):
            print("i like geeks for geek ")
            print("the summation of values :{}".format(x+y))
            func(*args,**kwargs)
        return wrapper
    return inner

def function(*args):
    for i in args:
        print(i)
decorator_fun(10,15)(function)('geeks','for','geek')

