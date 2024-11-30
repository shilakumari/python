class MyClass:
    def __init__(self):
        self.arg1=0
        self.arg2=0

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

obj1 = MyClass(10,20)
obj2 = MyClass(30,2)
print(obj1.arg1)
print(obj2.arg2)