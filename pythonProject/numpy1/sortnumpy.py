import numpy as np

arr=np.array([[1,4,3,2],
              [7,5,6,4],
              [5,7,8,9]])

print(np.sort(arr,axis=0,kind="mergesort"))

dtypes=[("name",'S10'),("rollno",int),("cgpa",float)]
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
print(dtypes)
print(values)
arr=np.array(values,dtype=dtypes)
print(arr)
print(np.sort(arr,order='rollno'))