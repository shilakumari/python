#List
l1=list(range(10))
print(l1)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2=l1[3:7]
print(l2)#[3, 4, 5, 6]
print("id(l1)",id(l1),"id(l2)",id(l2))#id(l1) 1882163379840 id(l2) 1882159716544
l3=l1[:10]
print(l3)
print("id(l1)",id(l1),"id(l3)",id(l3))#id(l1) 1479830535808 id(l3) 1479827503936

#Dictionary
#Using function as key, new id generate for function
d={1:lambda x:x**2,2:lambda x:x**3, lambda x:x**4:3}
print(d)

#stored key as function in a variable, by modifying function as constant value, using as key
f=lambda x:x**5
print(id(f),"and", id(lambda x:x**5))#2158519221472 and 2158519221632
print(d)

d[f(2)]=34
print(d)

#tuple
t1=("a","b","c","d")
print(t1[0])#a
print(t1[-1])#d
print(t1[1:3])#('b', 'c')

t1=("a","b","c")
x,y,z=t1
print(x,y,z)

t1=("a","b","c")
print(t1.count("a"))#1
print(t1.index("a"))#0

#find min and max in a tuple without using built-in function
tuple1=(5, 10, 3, 15, 2, 20)
minV=tuple1[0]
maxV=tuple1[0]
for i in tuple1:
    if maxV<i:
        maxV=i
    if minV>i:
        minV=i
print(minV, maxV)#2 20

#Set
set1={1,2,3,4}
set1.add(4)
print(set1)#{1, 2, 3, 4}

set1.discard(2)
print(set1)#{1, 3, 4}

#remove_element=set1.pop()#removes arbitrary elements
print(set1.pop())#1
print("Set after pop",set1)#Set after pop {3, 4}

s1={1,2,3}
s2={3,4,5}
#union
print(s1|s2)#{1, 2, 3, 4, 5}
print(s1.union(s2))#{1, 2, 3, 4, 5}
#Intersection
print(s1&s2)#{3}
print(s1.intersection(s2))#{3}
#Difference
print(s1-s2)#{1, 2}
#Symmetric Difference
print(s1^s2)#{1, 2, 4, 5}

a=print("ab")
b=print("abc")
dict1={a:1,b:2}
print(dict1)#{None: 2}