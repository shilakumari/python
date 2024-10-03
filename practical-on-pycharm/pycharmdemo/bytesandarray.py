lst=[20,30,40,50,60,70,80]
b=bytes(lst)#Indexing,slicing,reputation not allowed
print(type(b))
#b[2]=33


b1=bytearray(lst)#slicing,reputation not allowed
print((type(b1)))
b1[0]=10
for i in b1:
    print(i)