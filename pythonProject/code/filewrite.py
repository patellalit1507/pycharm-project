#file=open("geeks.txt","w")
x=int(input())
file=open("geeks.txt",'w')
for i in range(10):
    file.write("{} \n".format(x*(i+1)))

file.close()
file=open("geeks.txt",'r')
print(file.read())
file.close()