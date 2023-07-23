class employee():
    def __init__(self):
        print("constructor is called ")

    def __del__(self):
        print("destructor is called")

def call_class():
    print("we are in call function")
    obj=employee()
    print("function ends")
    return obj

obj=call_class()
#del obj   ---- this will delete refrence of object so dectructor will firstly called then print programm end
#del obj
print("programm ends")