c = "eabcd efg hija"
print("length:" ,len(c))

print("max : ",max(c)) # j is alphaticaly number is highest value

print("min : ",min(c))#space is a lowest value

print("min:",min("abcd"))

print("short :",sorted(c)) # in ascending order

print("short reverse :", sorted(c,reverse=True)) # in descending order
print("capitalize : ",c.capitalize()) # first letter is capital and rest is small
print("title: ",c.title()) # first letter of each word is capital and rest is small
print("upper: ",c.upper()) # all letter is capital
print("lower: ",c.lower()) # all letter is small
print("count", c.count("a")) # count the dublicte string
print("find: ",c.find("a")) # its shows index of first a
print("find: ",c.find("a", 2)) # its shows index of first a after index 2
print("index: ",c.index("a")) # its shows index of first a

#diff between find and index
print("find: ",c.find("z")) # its shows -1 if string is not found    
# print("index: ",c.index("z")) # its shows error if string is not found

print("startswith: ",c.startswith("e")) # its shows true if string starts with e
print("endswith: ",c.endswith("a")) # its shows true if string ends with a

#format string
name = "John"
age = 30
print("my name is {} and i am {} years old".format(name, age)) # its shows my name is John and i am 30 years old
print("my name is {1} and i am {0} years old".format(name, age)) # its shows my name is John and i am 30 years old

print("diggit: ",c.isdigit()) # its shows false if string is not digit
print("123".isdigit()) # its shows true if string is digit
print("split: ",c.split("a"))

lists = ["a","b","c","d" ,"e","f","g","h","i","j"]
print("joins : ","b".join(lists)) # its shows a b c d e f g h i j
print("joins : "," ".join(lists)) # its shows a b c d e f g h i j

print("replce: ",c.replace("a", "x")) # its shows ebcxd efg hijx  
srting = "                         h                     "
print("strip: ",srting.strip()) # its shows h
print("find: ",c.find("a", 2)) # its shows index of first a after index 2



