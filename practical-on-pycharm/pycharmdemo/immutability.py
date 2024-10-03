a=10
b=10
print(id(a))#140704259443416
print(id(b))#140704259443416
print(a is b)#True

a=True
b=False
print(id(a))#140704258642512
print(id(b))#140704258642544
print(a is b)#False

a="Shila"
b="Shila"
print(id(a))#1833756275744
print(id(b))#1833756275744
print(a is b)#True