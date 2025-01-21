f1=open("sample.txt","r")
#print(f1.readlines())#['1\n', '2\n', '3\n', '4\n', '5']
print(f1.readlines(2))#['1\n', '2\n']
print(f1.readlines(3))#['3\n', '4\n']
print(f1.readlines(1))#['5']
print(f1.readlines(1))#[]
f1.close()
