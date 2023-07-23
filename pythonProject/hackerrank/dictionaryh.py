
dict={}
for i in range(int(input())):
    line=input().split()
    dict[line[0]]=sum(map(float,line[1:]))/3
k=input()
#s=sum(dict[k])
print("{:.2f}".format(dict[k]))