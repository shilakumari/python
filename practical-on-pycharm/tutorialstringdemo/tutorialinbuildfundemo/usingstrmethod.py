class Person:
    def __init__(mySelf, name, age):
        mySelf.name=name
        mySelf.age=age

    def __str__(self):
        return f"Hello, my name is: {self.name} and age {self.age}"

p = Person("Shiela", 28)
print(p)#Hello, my name is: Shiela and age 28

x=10
def foo():
    global x
    x+=1

print(x)