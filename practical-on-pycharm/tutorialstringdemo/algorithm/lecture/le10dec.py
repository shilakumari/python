#MRO
"""class Sparrow:
    def swim(self): print("The sparrow is swimming")
class Swan(Sparrow):
    def swim(self): print("The swan is swimming")
class Albatross(Swan,Sparrow):pass
birds=[Sparrow(),Swan(),Albatross()]
for bird in birds:
    bird.swim()
#It prints the lookup order
print(Albatross.__mro__)
#(<class '__main__.Albatross'>, <class '__main__.Swan'>, <class '__main__.Sparrow'>, <class 'object'>)
print(Albatross.mro())
#[<class '__main__.Albatross'>, <class '__main__.Swan'>, <class '__main__.Sparrow'>, <class 'object'>]
"""
#Late Binding
#A list to hold lambda function
"""funcs=[]
for i in range(3):
    funcs.append(lambda:i)
for fun in funcs:
    print(fun(), end=" ")#2 2 2
"""
#Controlling Late Binding
funcs=[]
def create_lambda(x):
    return lambda:x
for i in range(3):
    funcs.append(create_lambda(i))
for fun in funcs:
    print(fun(), end=" ")#0 1 2
