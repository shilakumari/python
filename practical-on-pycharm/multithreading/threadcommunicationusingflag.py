from threading import *
from time import sleep

class Producer:
    def __init__(self):
        self.products = []
        self.orderPlaced = False

    def produce(self):
        for i in range(1,5):
            self.products.append("Product"+str(i))
            sleep(1)
            print("Item added")
        self.orderPlaced = True

class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        #while not self.prod.orderPlaced:
        while self.prod.orderPlaced == False:
            print("Waiting for the orders")
            sleep(0.2)
        print("Order shipped ",self.prod.products)

p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()