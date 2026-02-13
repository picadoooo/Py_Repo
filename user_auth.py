User_Name = input("Enter your user name: ")
User_password = input("Enter your password: ")

if User_Name == "admin" and User_password == "1234":
    print("Access granted")
elif User_Name == "admin" and User_password != "1234":
    print("Incorrect password")
    input("Enter your password: ")    
else:
    print("Access denied")
