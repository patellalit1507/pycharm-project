def sortsecond(val):
    return val[1]

N=int(input())
list=[]

for i in range(N):
    name=input()
    grade=float(input())
    list.append([name,grade])

list.sort(key=sortsecond)
#print(list)
#print(list[N-2][1])
#print(list)



for i in list:
  if(i[1]>list[0][1]):
      k=i[1]
      break

for i in list:
    if(i==k):
        print(i[0])

