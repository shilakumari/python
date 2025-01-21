#abstract base class
"""from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print_data(self):
        pass
class Report(Printable):
    def print_data(self):
        print("Report: Sales Data")

r=Report()
r.print_data()#Report: Sales Data
"""
#Duck typing
class Printer:
    def print_data(self):print("Printer:Document")
def use_printer(obj):
    obj.print_data()
p=Printer()
use_printer(p)#Printer:Document