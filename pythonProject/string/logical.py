str1='hiii jddkddkdd  ejkdld'
str2='greeks for greeek is the'
#repr is used to print string with quotesm ' '
print(repr(str1 and str2))
print(repr(str2 and str1))

#pythonPython considers empty strings as having boolean value of ‘false’ and non-empty string as having boolean value of ‘true’.
#For ‘and’ operator if left value is true, then right value is checked and returned. If left value is false, then it is returned

print(repr(str1 or str2))
print(repr(str2 or str1))
#For ‘or’ operator if left value is true, then it is returned, otherwise if left value is false, then right value is returned.

#note:-  bitwise operators like (|,&) dont work in string
print(id(str1))
print(id(str2))
print(str2.find("kall"))
str2=str.upper(str2)
print(str2)
str1=str.title(str1)
print(str1)

