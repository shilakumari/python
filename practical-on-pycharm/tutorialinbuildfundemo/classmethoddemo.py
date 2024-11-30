class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    @classmethod
    def fromString(cls, carStr):
        make, model,year = carStr.split("-")
        return cls(make,model,year)
myCar = Car.fromString("Honda-Civic-2022")
print(myCar.model) #Civic


