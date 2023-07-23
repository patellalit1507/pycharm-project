from sys import maxsize

def Create_stack():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,key):
    stack.append(key)
    print(key + " pushed to stack")

def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize-1)
    return stack.pop()








stack=Create_stack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
pop(stack)
print(stack)

