from threading import *
from time import sleep


class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats

    def buy(self,seatsRequested):
        print("Total number of available seats: ",self.availableSeats)
        if self.availableSeats>=seatsRequested :
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the Ticket")
            self.availableSeats -= seatsRequested
        else:
            print("Sorry, no seats available")

obj = BookMyBus(10)
t1 = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(4,))
t3 = Thread(target=obj.buy, args=(3,))

t1.start()
t2.start()
t3.start()

