import re

regix=r"([a-Az-Z]+)(\d+)"
print(regix)
write=re.search(regix,"I was born on 24")
#print(write)