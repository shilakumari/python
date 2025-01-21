lst=[10,20,"Bharath",-10,30.5]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*2)
print(len(lst))

#Adding and removing in list
lst.append(40)
lst.insert(3,46)
lst.remove("Bharath")
del(lst[2])
print(lst)

#lst.clear()
print(min(lst))
print(max(lst))
lst.sort(reverse=True)
print(lst)

#Tuple
tpl=(40, 50, 50, "Bharath")
#tpl[1]=88
print(tpl[2])
print(tpl*3)
print(tpl.count(50))
print(tpl.index("Bharaths"))