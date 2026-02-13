import math as m

print(m.ceil(19.19456456)) #ager 0.5 se zaada ho to next integer ko return karta hai
print(m.floor(19.19456456)) #
print(m.floor(19.4)) 

print(m.fabs(19.19456456)) #absolute value return karta hai
print(m.copysign(19.4456456, -0.00))
print(m.factorial(5))
print(m.fmod(10, 3)) # modulus operator ka alternative hai
print(m.frexp(10)) # return the mantissa and exponent of a number
print(m.fsum([1, 2, 3, 4, 15])) # sum of a sequence of numbers
print(m.isinf(float('inf'))) # check if the number is infinite
print(m.isnan(float('nan'))) # check if the number is NaN (not a number
print(m.ldexp(0.5, 5)) # return the result of x * (2**i)
print(m.modf(19.19456456)) # return the fractional and integer parts of a number
print(m.trunc(19.19456456)) # return the integer part of a number, truncating towards zero

print("---------------------------------------------------------------------------")

#power and logarithmic functions
print(m.exp(10)) # return the exponential of a number
print(m.expm1(10)) # return the exponential of a number minus 1
print(m.log(10)) # return the natural logarithm of a number 
