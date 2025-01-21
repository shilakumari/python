"""default_value=input("Enter default value")
#Assume the user inputs: Initial Default
def display(value=default_value):
    print("value",value)
default_value="changed default"
display()#value  Initial Default
display("New Input")#value New Input"""

d={"1,1":1}
d11=d.get("1,1",0)#default value is 0
print(d11)
d12=d.get("1,2",0)
print(d12)
print(d.get("1,3",0))
print(d.get("2,3",0))
print(d.get("100,3",0))

#
"""l={1:4,2:7}
v=l.pop(2)
print(v)

l={1:4,2:7}
del l[2]
print(l)

l={1:4,2:7}
l.popitem()
print(l)
l.clear()
print(l)"""

l={1:4}
l.update({2:4,4:5})
print(l)#{1: 4, 2: 4, 4: 5}