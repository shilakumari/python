dict={1:"Bob",2:"Bill",3:"Joy"}
print(dict)

k=dict.keys()
for i in k:
    print(i)

v=dict.values()
for i in v:
    print(i)

print(dict[2])#print dict of key=2

#To delete from dictionary use del function
del dict[2]
print(dict)