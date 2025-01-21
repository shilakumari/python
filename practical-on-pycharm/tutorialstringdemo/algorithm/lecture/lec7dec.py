#MRO demo
"""class Engine:
    def start(self):print("Engine starting.")
class Radio:
    def start(self):print("Radio playing.")
class Car(Engine,Radio):
    pass
c1=Car()

c1.start()#Engine starting.
print(Car.__mro__)"""

#Multiple Inheritance
"""class WaterVehicle:
    def move(self):
        print("Moving on water.")
class AirVehicle:
    def move(self):
        print("Moving in air.")

class HoverDraft(WaterVehicle,AirVehicle):
    pass
hc=HoverDraft()
hc.move()#Moving on water.
print(HoverDraft.__mro__)
#(<class '__main__.HoverDraft'>, <class '__main__.WaterVehicle'>, <class '__main__.AirVehicle'>, <class 'object'>)
"""
#Late binding
class Greater:
    def greet(self):
        print("Hello")
g=Greater()
g.greet()#Hello

#Change greet() method at runtime
def new_greet(self):
    print("Hi there!")

Greater.greet=new_greet
g.greet()#Hi there!