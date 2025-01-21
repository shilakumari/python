from functools import reduce


def cube(n):
    return n*n*n
print(cube(10))
#cube of n
fun = lambda n:n**3
print(fun(10))

#even or odd
f = lambda n: 'Yes' if n%2==0 else 'No'
print("Is even: ",f(10))

#Calculate sum of two numbers
f1 = lambda x,y: x+y
print(f1(30,20))

#Retrieve only even numbers from a list
lst=[10, 2, 33, 45, 89,2]
f2 = list(filter(lambda a:a%2==0,lst))
print(f2)
for i in f2:
    print(i)

#Double the list value
f3 = list(map(lambda a:a*2,lst))
print(f3)
for i in f3:
    print(i)

#Sum of all elements in a list
result = reduce(lambda a,b:a+b,lst)
print("Sum of all elements in a list:",result)

#