m=int(input())
l=[]
for i in range(m):
	a,b=input().split()
	l.append(a)
	l.append(b)
#print(l)
j=0

for i in range(m):
	try:
		k=int(l[j])//int(l[j+1])
		print(k)
		j=j+2
	except (ZeroDivisionError,IndexError,ValueError) as e:
		print("Error Code:",e)
		j=j+2


