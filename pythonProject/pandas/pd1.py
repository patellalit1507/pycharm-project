import pandas as pd
p1=pd.Series([1,2,3,4])
print(p1)
p2=pd.read_csv("book.csv")
print(p2)
p3=p2.iloc[0:3,0:2]
print(p3)