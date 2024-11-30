class Dog:
    species = "Canine" #class attribute
    def __init__(self, name):
        self.name = name #instance attribute

dog1  = Dog("Buddy")
dog2 = Dog("Charlie")
print(dog1.species)
print(dog2.species)
