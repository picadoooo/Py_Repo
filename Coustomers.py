class Coustomers :

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
def check_name(Coustomers) :  
        if Coustomers.gender == "male":
            print("hello mr {}".format(Coustomers.name))
        else :
            print("hello mis {}".format(Coustomers.name))

cust = Coustomers("wasim","male")

check_name(cust)

        