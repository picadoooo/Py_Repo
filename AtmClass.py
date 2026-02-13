class AtmClass :
    def __init__(self):
     self.__pin = ''
     self.__balance = 0
   #   self.menu()

   #  def menu(self):
   #     user_input = input(""" 
   #                       Hello what would like print
   #                       1.Enter 1 to create __pin.
   #                       2.Enter 2 to deposit.
   
   #                       3.Enter 3 to withdrawal.
   #                       4.Enter 4 to check __balance.
   #                       5.Enter 5 to exit. 
   #                       """)
   #     match user_input :
   #        case "1" : 
   #          self.carte_pin()
   #          # self.menu()


   #        case "2" :
   #           self.deposit()
   #          #  self.menu()


   #        case "3":
   #           self.withdrawal()
   #          #  self.menu()

             

   #        case "4":
   #           self.Check_balance()
   #          #  self.menu()
   #        case _:
   #           print("bye") 
    
    def  carte_pin(self) :
       self.__pin = input("Enter your pin")
       print("pin set successfully")
      #  self.menu()

    def deposit(self):
       temp_pin = input("Enter your pin : ")
       if temp_pin == self.__pin :
          amount =input("Enter your amount :")
          

          if(amount.isdigit) :
             self.__balance += int(amount)
             print("Deposit successfully")
          else:
             print("plz Enter digit")   
       else : 
          print("your __pin is wrong")

    def withdrawal(self) :
       temp_pin = input("Enter your pin : ")

       if temp_pin == self.__pin :
         amount =input("Enter your amount :")

         if(amount.isdigit) :
             if self.__balance >= amount:
                self.__balance -= int(amount)
                print("withdrawal successfully")
             else :
                print("indecent balance")   
         else : 
            print("plz enter debit")    
       else : 
          print("your __pin is wrong")

    def Check_balance(self) :
        temp_pin = input("Enter your pin : ")
        if temp_pin == self.__pin :
           print("balance :",self.__balance)
        else :
           print("Invalid pin")
            




          
         
              

           
               
          

          