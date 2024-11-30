class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(f"Car: {self.make} {self.model} {self.year}")
myCar = Car("Honda", "Civic", 2022)
print(myCar.model) #Civic
myCar.display() #Car: Honda Civic 2022

