l1=[1,2,2,3,4,5,3,6,4]
#o/p:[1,5,6]
d1={}
for ele in l1:
    if ele not in d1.keys():
        d1[ele] = 1
    else:
        d1[ele] += 1
print(d1)

l1=[]
for key in d1.keys():
    if d1[key] == 1:
        l1.append(key)
print(l1)