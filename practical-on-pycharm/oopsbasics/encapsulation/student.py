class Student:

    def __init__(self):
        # to make private use __
        self.__id =123
        self.__name="John"

    def display(self):
        print(self.__id)
        print(self.__name)

s1=Student()
#print(s1.__id)
#print(s1.__name)
s1.display()

#Using Name Mangling, we can access private field directly
print("Student id using Name Mangling:",s1._Student__id)
print("Student name using Name Mangling:",s1._Student__name)
