str=input()

for i in str:
    count=0
    if(i.isalnum()):
        count=count+1
        break
if(count==1):
    print("True")
else:
    print("False")

for i in str:
    count=0
    if(i.isalpha()):
        count=count+1
        break
if(count==1):
    print("True")
else:
    print("False")

for i in str:
    count=0
    if(i.isdigit()):
        count=count+1
        break
if(count==1):
    print("True")
else:
    print("False")

for i in str:
    count=0
    if(i.isupper()):
        count=count+1
        break
if(count==1):
    print("True")
else:
    print("False")

for i in str:
    count=0
    if(i.islower()):
        count=count+1
        break
if(count==1):
    print("True")
else:
    print("False")
