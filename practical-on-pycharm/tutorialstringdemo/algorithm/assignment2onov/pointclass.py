import math


class Point:
    def __init__(self):
        self.x=0
        self.y=0
    def __init__(self,x:int, y:int):
        self.x=x
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self,x1):
        self.x=x1
    def set_y(self, y1):
        self.y = y1
    def distance(self):
        dist:float = math.sqrt((self.x-0)**2+(self.y-0)**2)
        return dist
    def distance(self,x2=0,y2=0):
        dist:float = math.sqrt((self.x-x2)**2+(self.y-y2)**2)
        return dist
    def distance2(self,point):
        dist: float = math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        return dist

first=Point(6,5)
second=Point(3,1)
print("distance(0,0)=",first.distance())#distance(0,0)= 7.810249675906654
print("distance(second)=",first.distance2(second))#distance(second)= 5.0
print("distance(2,2)=",first.distance(2,2))#distance(2,2)= 5.0
print("distance()=",first.distance())#distance()= 7.810249675906654
