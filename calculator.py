print("Welcome to the Python Calculator!")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


print("""
          presse + for addition
          presse - for subtraction
          presse * for multiplication
          presse / for division
          presse % for modulus
          presse ** for exponentiation
          presse // for floor division
        
             """)
match input("Enter the operator: "):
        case "+":
         print("The sum is: " + str(num1 + num2))
        case "-":
         print("The difference is: " + str(num1 - num2))
        case "*":
         print("The product is: " + str(num1 * num2))
        case "/":
         print("The quotient is: " + str(num1 / num2))
        case "%":
         print("The remainder is: " + str(num1 % num2))
        case "**":
         print("The result of num1 raised to the power of num2 is: " +
            str(num1 ** num2))
        case "//":
         print("The result of floor division is: " + str(num1 // num2))
        case _:
         print("Invalid operator! Please try again.")



