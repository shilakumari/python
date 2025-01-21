tpl1=(30,)
print(type(tpl1))
tpl2=(30)
print(type(tpl2))

tpl=(20,30,20,"xyz")
print(type(tpl))
print(tpl*3)
print(tpl.count(20))
print(tpl.index("xyz"))

#list to tuple
lst=[10, 20, 30, "Hello"]
tpl3=tuple(lst)
print(type(tpl3))

