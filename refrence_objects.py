import sys as s

a= 10
b = a 
c= b

a= 20

del a
print(b)

print(s.getrefcount(b))