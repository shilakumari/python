#Cubes of integers from 1 to 10
"""lst=[]
for i in range(1,11):
    lst.append(i**3)
print(lst)"""
lst1 = [i**3 for i in range(1, 11)]
print(lst1)

#Even numbers from 1 to 10
"""lst=[]
for i in range(1,11):
    if i%2==0:
        lst.append(i)
print(lst)"""
lst2 = [i for i in range(1, 11) if i%2==0]
print(lst2)

#Product of two numbers list
a=[1,2,3,4,5]
b=[10,20,30,40,50]
"""z=[]
for i in range(len(a)):
    z.append(a[i]*b[i])
print("Product of two list: ",z)"""
lst3=[a[i]*b[i] for i in range(len(a))]
print("Product of two list: ",lst3)

#Create list of common elements of two list
a1=[1,2,3,4]
b1=[2,4,6,8]
"""z1=[]
for i in a1:
    if i in b1:
        z1.append(i)
print(z1)"""

lst4=[i for i in a1 if i in b1]
print(lst4)