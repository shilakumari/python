class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Start the car")

    def stop(self):
        print("Stopping the car")


class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        # Without super()
        # BMW.__init__(self,make,model,year)
        # With super()
        super().__init__(make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled

    def start(self):
        super().start()
        print("Button start")

    def display(self):
        print("cruiseControlEnabled:",self.cruiseControlEnabled)

class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        # BMW.__init__(self, make, model, year)
        # With super()
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def display(self):
        print("parkingAssistEnabled:",self.parkingAssistEnabled)


threeSeries=ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries=FiveSeries(True,"BMW","G60","2024")
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()
fiveSeries.display()
