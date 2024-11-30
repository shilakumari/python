class Product:
    def __init__(self):
        self.name="IPhone"
        self.description="Its awesome"
        self.price=700

    def __del__(self):
        print("Inside the destructor")

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p1=Product()
p1.display()
#p1=None#for garbage collector

p2=Product()
p2.display()


