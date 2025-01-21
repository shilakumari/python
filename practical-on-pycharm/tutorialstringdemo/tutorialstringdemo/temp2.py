"""class A:
    x=1
a1=A()
a2=A()
a1.x=2
print(a1.x,a2.x,A.x)

lambda_add = lambda x,y: x-y
print(lambda_add(4,3))
print(lambda_add(3,4))


def subtract(bigger=4, smaller=2):
    return bigger - smaller
print(subtract())#2
print(subtract(smaller=3, bigger=4))#1"""

def cube(x):
    return x*x*x
print(cube(2)) #4
print(cube(-3)) #9

s = input("give me a string:")
print(s)
lambda_dist = lambda x1,y1,x2,y2:((x2-x1)**2 + (y2-y1)**2)**0.5 #0.5 means square-root
print(lambda_dist(0,0,2,2))