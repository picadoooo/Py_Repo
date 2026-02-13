class fracation :
    def __init__(self ,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return "{}/{}".format(self.num1,self.num2)    
    
    def __add__(self,other):
        add = self.num1 * other.num1
        add2 = self.num2 * other.num2   
        return "{}/{}".format(add,add2)
