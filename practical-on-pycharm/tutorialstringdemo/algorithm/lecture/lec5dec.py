"""l1d=[1]*3
print(l1d)#[1, 1, 1]
l2d=[[1]*3]*3
print(l2d)#[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
l2d[0][1]=0
print(l2d)#[[1, 0, 1], [1, 0, 1], [1, 0, 1]]

l=[1,2]
l.append(l)
print(l)#[1, 2, [...]], every l has l inside it
print(len(l))#3
print(l[2])#[1, 2, [...]]
print(l[2][2])#[1, 2, [...]]

#set
s={1,2,3,4,5}
s.add((6,7))
print(s)#{1, 2, 3, 4, 5, (6, 7)}

#tuple
t=(1,2,3,[4,5])
#t[0].append(6)#AttributeError
print(t)

t[3].append(4)#No error, because at index 3 is list, so append in list allowed.
print(t)#(1, 2, 3, [4, 5, 4])
"""

"""class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    pass

d1=Dog()
d1.eat()#Eating..."""

"""class Vehicle:
    def move(self):
        print("Moving...")
class Car(Vehicle):
    def drive(self):
        print("Driving a car.")
car1=Car()
car1.move()#Moving...
car1.drive()#Driving a car."""

#Multiple inheritance
"""class Flyer:
    def __init__(self):self.wings=True
    def fly(self):
        print("Flying...")
class Swimmer:
    def __init__(self):self.fins=True
    def swim(self):
        print("Swimming...")
class Duck(Flyer,Swimmer):
    pass

daffy=Duck()
daffy.fly()#Flying...
daffy.swim()#Swimming...
print(daffy.wings)#True
print(daffy.fins)#AttributeError: 'Duck' object has no attribute 'fins'.
"""

#Multilevel Inheritance
"""class Organism:
    def live(self):
        print("Living...")
class Animal(Organism):
    pass
class Bird(Animal):
    def fly(self):
        print("Flying...")
sparrow=Bird()
sparrow.live()#Living...
sparrow.fly()#Flying...
"""

#Hierarchical Inheritance
"""class Shape:
    def draw(self): print("Drawing shape...")
class Circle(Shape):pass
class Square(Shape):pass
c=Circle()
s=Square()
c.draw()#Drawing shape...
s.draw()#Drawing shape...
"""

#Method overriding
"""class Animal:
    def speak(self):print("Animal makes a sound.")
class Cat(Animal):
    def speak(self):print("Cat meows.")
whiskers=Cat()
whiskers.speak()#Cat meows.
"""

#super()
class Logger:
    def log(self,message):
        print(f"Log:{message}")
class AdvanceLogger(Logger):
    def log(self,message):
        super().log(message)
        print(f"Advance Log:{message}")
logger=AdvanceLogger()
logger.log("System error")
#output:
#Log:System error
#Advance Log:System error