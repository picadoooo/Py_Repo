import math as m
def Even_Odd(i) :
    "hello this is even odd function"
    if i%2 == 0 :
        return "even"
    else :
     return "odd"

for i in range(1,5) :
  print(Even_Odd(i))


def power(a=1,b=1):
   return a**b


print(power(10,10))
print(power(b=10,a=20))


def cal(*numbers):
   print(numbers)
   product = 1
   for i in numbers:
      print(product*i)
      product += i

cal(10,20,30,40)