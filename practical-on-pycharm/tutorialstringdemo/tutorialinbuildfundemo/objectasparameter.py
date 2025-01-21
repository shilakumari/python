from temp import Example
class Mydetails:
    def __init__(self, obj):
        self.obj = obj

obj = Example()
print(type(obj))#<class 'temp.Example'>
myDetailsObj = Mydetails(obj)
print(type(myDetailsObj))#<class 'temp.Example'>

myDetailsObj.obj.instanceMethod()
