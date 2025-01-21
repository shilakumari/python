x=10
def foo():
    global x
    x += 1
    print(x)

foo()

fruit=["a","b","c","c"]
print(fruit[1:3])
print(fruit[:2])
print(fruit[::2])

fruit.append("blueberry")
print(fruit)

a=[]
for x in range(4):
    a.append(x**2)
print(a)#[0, 1, 4, 9]

#Tuple is extendable
t=(1,2,3)
print(id(t))#2901278465856
t2=(4,)
t = t + t2
print(id(t))#2901278028272
print(t)
#t[1] = 4#Not allowed modification


#List
lst1=[1,2]
print(id(lst1))#2829187946688
lst1.append(3)
print(id(lst1))#2829187946688
lst1 = lst1 + [4]
print(id(lst1))#2829190933312

#List Comprehension
sqr = [x**2 for x in range(1,6)]
print(sqr)

#List methods and functions
ls1 = [6,1,3]
print(id(ls1))#2184916347712
ls1.sort()
print((id(ls1)))#2184916347712
print(ls1)#[1,3,6]

#String
print("abc".find("a"))#0
print("abc".find("z"))#-1
#print("abc".index("z"))#ValueError: substring not found

s="xyz"
t=((s.find("y")),(s.find("b")))
print(t)#(1,-1)

print("abc"[::-1].find("bc"))#-1

print("12345.0".isdigit())#False
print("12345".isdigit())#True

print(" \nrtykj ssdf gfg \t jk\t\n".strip())#rtykj ssdf gfg 	 jk
print(" \nrtykj ssdf gfg \t jk\t\n".lstrip())
print(" \nrtykj ssdf gfg \t jk\t\n".rstrip())
