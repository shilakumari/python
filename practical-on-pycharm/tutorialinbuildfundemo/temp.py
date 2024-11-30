class Example:
    @staticmethod
    def staticMethod():
        print("Static method called")

    def instanceMethod(self):
        print("Instance method called")
        Example.staticMethod()

obj = Example()
obj.staticMethod()
obj.instanceMethod()

class MyClass:
    classVar = 0
    def __init__(self):
        self.instance_var = MyClass.classVar
        MyClass.classVar += 1
a = MyClass()
b = MyClass()
c = MyClass()
print(a.instance_var, b.instance_var, c.instance_var)#0 1 2

