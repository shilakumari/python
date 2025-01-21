myVaryingTuple = ("str", 1, 1.3, True)
print(myVaryingTuple)

#Tuple is ordered and immutable, when want changes then covert in list
l1 = list(myVaryingTuple)
l1.append("Shila")
print(tuple(l1))#('str', 1, 1.3, True, 'Shila')

#We can not change the "Tuple", but we can extend it.
t1 = ("a", "b", "c")
y = ("d",)
t1 += y
print(t1)

#unpacking tuple
(a,b,c,d) = t1
print(a)
print(b)
print(c)
print(d)

tuples1 = (1,2,3)
tuples2 = (4, 5, 6)
result = tuples1+tuples2*2
print(result)#(1, 2, 3, 4, 5, 6, 4, 5, 6)

#tuple constructor
fruits = tuple(("apple", "banana", "cherry"))
print(type(fruits))
print(fruits[1]) #banana
print(fruits[-1]) #cherry