sets = {1,2,3,4,5,6} #homoginis sets
sets2 = {1,"hello",22.2,True} #hydrognius set

sets3 = {1,1,1,2,2,2,3,3,3,4,4,4,5,5,5} #its remove all dublicate values
print(sets3)

# sets4 = {[1,2],[2,3]} # olny imutable values supoorts
sets5 = {(10,20),(10,30),(10,20)}
print(sets5) 

sets6 = {(1,2,3),("Hello")} # sets donst sapports index
print(sets6)

# sets7 = {{1,3}{2,4}} #we cannot create 2d or 3d sets

# print(sets6[1]) sets donst supports indexing
# print(sets6[0:3]) its not sapports to 
lis = list(sets6)
print(id(sets6))
print(lis)
lis[0] = "www" 
print(lis)
sets6 = set(lis)
print(sets6)
print(id(sets6))
sets6.add(10)
print(sets6)
# sets6 + sets2 cant do this

for i in sets6 :
    print(i)
sets7 = {1,24,5,6,4,8,1,34,34}    

print(sorted(sets7))
print("-"*100)
print(sets2.union(sets2))
