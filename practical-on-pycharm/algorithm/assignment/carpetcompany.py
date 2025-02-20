class Floor:
    def __init__(self,width:float, length:float):
        self.width = width
        self.length = length
    def get_area(self):
        return self.width * self.length

class Carpet:
    def __init__(self, cost:float):
        if cost<0:
            self.cost = 0
        else:
            self.cost = cost
    def get_cost(self):
        return self.cost

class Calculator:
    def __init__(self, floor:Floor, carpet:Carpet):
        self.floor=floor
        self.carpet=carpet
    def get_total_cost(self):
        return self.floor.get_area() * self.carpet.get_cost()

carpet = Carpet(3.5)
floor = Floor(2.75, 4.0)
calculator = Calculator(floor,carpet)
print("total=",calculator.get_total_cost())

carpet = Carpet(-1.5)
floor = Floor(5.4, 4.5)
calculator = Calculator(floor,carpet)
print("total=",calculator.get_total_cost())