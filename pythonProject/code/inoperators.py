list1=[1,2,3,5,6,7]
list2=[23,3,45,56,65,33]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")