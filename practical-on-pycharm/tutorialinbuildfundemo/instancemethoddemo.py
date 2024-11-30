class Person:
    #class variable
    place="Earth"
    def __init__(mySelf, name, age):
        mySelf.name=name
        mySelf.age=age

    #Instance method
    def fromString(mySelf2):
        print("Hello, my name is: ",mySelf2.name)

p = Person("Shiela", 28)
p.fromString()
print(p)#<__main__.Person object

p1=Person("ABC",20)
p2=Person("DEF",10)

print(p1.place)
print(p2.place)
print(Person.place)

p1.place="Moon"
print(p1.place)
print(p2.place)
print(Person.place)