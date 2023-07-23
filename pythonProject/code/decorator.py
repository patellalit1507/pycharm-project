def hellodecorator(func):
    def inner1():
        print("this is before function execution")

        func()
        print("this is after function execution")
    return inner1
@hellodecorator
def function_to_beused():
    print("this is inside function")

#function_to_beused=hellodecorator(function_to_beused)
function_to_beused()

