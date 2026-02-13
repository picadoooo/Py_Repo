x = 0
mul = 0

def loop1(number_mul, times_mul):
    global x, mul

    if x == times_mul:
        return mul

    mul += number_mul   # repeated addition
    x += 1
    return loop1(number_mul, times_mul)

m = loop1(5, 10)
print(m)
   
