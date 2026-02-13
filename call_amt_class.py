# import AtmClass

# atm = AtmClass.AtmClass()
# atm.menu()


from AtmClass import AtmClass   # import class
# from fracation import fracation 

# user_one = AtmClass()    # object create
# user_one.carte_pin()
# user_one.deposit()
# print(user_one.balance)

user_two = AtmClass()
# user_two.carte_pin()
# user_two.deposit()
# user_two.Check_balance()
user_two._AtmClass__balance = "1234"
print(user_two._AtmClass__balance)



# subject = fracation(10,20)
# # subject2 = fracation(20,30) 
# print(subject + subject , type(subject))
        
