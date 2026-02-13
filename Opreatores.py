#arathmatic operators in python
a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

#relational operators in python
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical operators in python
print(a>5 and b>15)
print(a>5 or b>15)
print(not(a>5 and b>15))


#bitwise operators in python
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 2) # Left Shift
print(a >> 2) # Right Shift

#assignment operators in python
a = 10
a += 5  # Equivalent to a = a + 5
print(a)
a -= 3  # Equivalent to a = a - 3
print(a)    
a *= 2  # Equivalent to a = a * 2
print(a)
a /= 4  # Equivalent to a = a / 4
print(a)
a %= 3  # Equivalent to a = a % 3
print(a)
a **= 2  # Equivalent to a = a ** 2
print(a)
a //= 2  # Equivalent to a = a // 2
print(a)

print(5>>2)
#membership operators in python
lst = [1, 2, 3, 4, 5]
print(3 in lst)  # True
print(6 in lst)  # False
print(3 not in lst)  # False
print(6 not in lst)  # True
