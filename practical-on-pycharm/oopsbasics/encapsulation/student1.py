from tkinter.font import names


class Student1:

    # Using mutator/setter and accessor/getter method to achieve encapsulation
    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

s1=Student1()
s1.setId(123)
s1.setName("john")
print(s1.getId())
print(s1.getName())
