#a1=[1,2,2,3,4,5]
#a2=[4,4,3,2,1,1]
a1=[1,2,3,5,8,8]
a2=[8,8,6,5,3,2,1,1]
#o/p:6
n=len(a1)
c=0
for i in range(n):
    #print("a2",a2[n - 1 - i])
    #print("a1",a1[i])
    for j in range(n-i,-1,-1):
        print(a2[j],end=" ")
    print()

print(c)




"""from threading import Thread

def task():
    print("Task executed")
    print("wqd")
t = Thread(target=task)
t.run()
t.start()
"""

"""class MyClass:
    def __str__(self):
        return "MyClass __str__"
    def __repr__(self):
        return "MyClass __repr__"
obj = MyClass()
print([obj])
print(obj)
"""
