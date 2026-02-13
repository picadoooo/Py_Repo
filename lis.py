l = []
print(l)
l = [1, 2, 3, 4, 5] #homogenous it means that it can store only one type of data
print(l)
l2 = ["apple", "banana", "cherry",1,2,3,4] #hydroginys it mens that it can store any type of data
l3 = [1,3,4,5 ,[1,3,4,5,5]] #2d list
l3 = [[[1,2],[1,2]],[[1,2],[1,2]]] #3d list
print(l2)
print(l3)

l5 = list("abcdefghij") #empty 
print(l5)

print(l[0]) #accessing the first element of the list

l2 = ["apple", "banana", "cherry",1,2,3,4]
print(l2[4])
l3 = [1,3,4,5 ,[1,3,4,5,5]] #2d list
print(l3[4])
print(l3[4][0])

l3 = [[[1,1],[1,2]],[[1,3],[1,4]]] #3d list4
print(l3[1][1][1])

#operations on list
l1 = [1,2,3]
l1.append(4) #add an element to the end of the list
l1.append([1,2]) #add an element to the end of the list
print(l1) # adds only one item at the end of the list
l1.extend([5,6,7]) #add multiple elements to the end of the list    
print(l1) # adds multiple items at the end of the list
l1.extend('hello') #add multiple elements to the end of the list
print(l1) # adds multiple items at the end of the list
l1.insert([5][0],'x') #insert an element at a specific index
print(l1) # adds x at index 4


print(l1)
l1.remove('x') #remove an element from the list
print(l1) # removes x from the list


l1.pop() #remove the last element from the list
print(l1) # removes the last element from the list
l.clear() #remove all elements from the list its do emplpty list
print(l1) # removes all elements from the list its do emplpty list
l6 = l1 + l2 #concatenate two lists
print(l6) # concatenates l1 and l2
c = "eabcd efg hija"
str2 = "hello wasim how are you"
print("str2:",str2.find("e",2))
print("c",c.find("a",1)) # its shows the index of the first o after index 2
str3 = []
l7 = str2.split() #split a string into a list
print("split:",l7) # splits the string into a list of words
for i in  l7:
  str3.append(i.capitalize())
print(str3) # capitalizes the first letter of each word in the list  
print(" ".join(str3)) # joins the list into a string with a space between each word
print(str2[0:str2.find("o",2)]) # its shows the first word of the string

l1 = [1,1,2,3,3,4,4,5,5]
l2 = []

for i in l1 :
  if  i not in l2:
    l2.append(i) 

print(l2)   
