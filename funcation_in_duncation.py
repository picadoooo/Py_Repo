def outer_funcation() :
    def inner_funaction(a=10,b=20):
        def inner_in_innerfuncation(a,b):
           return a+b
        return inner_in_innerfuncation
    return inner_funaction

# val =   outer_funcation()()(10,20) 
# print(val)

str ="wasim"
a= 10
b =a
a=20


print(b,id(b) )
