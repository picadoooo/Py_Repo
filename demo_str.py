str1 = "hello"
print(id(str1))

print(id(str1.replace("h","w")))
print(str1.replace("h","2"))

b = 2
c = b
print(id(b))
print(id(c))

def abc(*a) :
    print(a)
abc(1,2,3,4,5)    
