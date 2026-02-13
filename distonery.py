D1 = {"name":"wasim","age":30}
D1.keys()
D1.values()

print(D1.keys(),D1.values())

print(D1)
print(D1["name"])
D1["name"] = 20
print("name" in D1)
print("*"*100)
for i in D1:
    print(i,":",D1[i])