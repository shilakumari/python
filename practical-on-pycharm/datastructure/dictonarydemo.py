person = {"name":"Shila", "age":28}
print(person["name"])#Shila
#Print dictionary
for item in person:
    print(item, person[item])

#update() to update dictionary
person.update({"addr":"Patna"})
print(person) #{'name': 'Shila', 'age': 28, 'addr': 'Patna'}

dict = {"a":1,"b":2,"a":3}
print(dict)#{'a': 3, 'b': 2}
print(dict.popitem())#('b', 2)
print(dict)#{'a': 3}

#access dictionary using get() or using "key"
d1 = {"a":1,"b":2,"c":3}
x=d1["b"]
print(x)#2
x1=d1.get("b")
print(x1)#2

#get key using keys()
x2=d1.keys()
print(x2)#dict_keys(['a', 'b', 'c'])

#get value using values()
x3 = d1.values()
print(x3)#dict_values([1, 2, 3])

#get key-value using items()
x4=d1.items()
print(x4)#dict_items([('a', 1), ('b', 2), ('c', 3)])

#add dictionary item
d2 = {"aa":1,"bb":2,"cc":3}
d2["name"]="Shila"
print(d2)#{'aa': 1, 'bb': 2, 'cc': 3, 'name': 'Shila'}