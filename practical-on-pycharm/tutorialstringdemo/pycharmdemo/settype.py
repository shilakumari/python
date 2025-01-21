s={10,20,30,"xyz",10,20}
s.update([50,60])
print(type(s))
print(s)

s.remove(10)
print(s)

#indexing, slicing and reputation not allowed in Set
#print(s[0])
#print(s[0:4])
#print(s*3)

#Frozen set
f=frozenset(s)
print(type(f))
#f.update([70,80])
#f.remove(50)
print(f)

