width=20
#print("hackerra".center(width," "))
#print("hackerra".ljust(width," "))
#print("hackerra".rjust(width," "))
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
k=1
for i in range(thickness+1):
    print((c*i)+"_"*(thickness-i))


