from abc import abstractmethod,ABC

class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled

    def start(self):
        super().start()
        print("Button start")

    def stop(self):
        print("Stopping the Threeseries")

    def display(self):
        print("cruiseControlEnabled:",self.cruiseControlEnabled)

    def drive(self):
        print("Three series is being driven")

class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        # BMW.__init__(self, make, model, year)
        # With super()
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def start(self):
        super().start()
        print("Remote start")

    def stop(self):
        print("Remote Stopping the Threeseries")

    def display(self):
        print("parkingAssistEnabled:",self.parkingAssistEnabled)

    def drive(self):
        print("Five series is being driven")


threeSeries=ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()

threeSeries.drive()

fiveSeries=FiveSeries(True,"BMW","G60","2024")
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()
fiveSeries.display()

fiveSeries.drive()

#b1=BMW("BMW","G60","2024")
