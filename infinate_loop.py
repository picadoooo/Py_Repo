x =1

def loop1():
    global x

    x+=1
    if(x==10):
      return "its an 10 value"
    else:
     return  loop2()
 
def loop2():
 return loop1()

m = loop2()
print(m)
