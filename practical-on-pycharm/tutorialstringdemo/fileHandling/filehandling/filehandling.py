f=open("sample.txt","w")#w- mean write mode
f.write("1\n")
f.write("2\n3\n4\n5")
f.close()

f1=open("sample.txt","r")#r- read mode
data=f1.read()
print(data)
f1.close()
#o/p:
    #1
    #2

#f2=open("sample.txt","r")
#f2.write("Hi")
#o/p: io.UnsupportedOperation: not writable

#Reading line by line
f3=open("sample.txt","r")
data=f3.readline()
print(data)#1
f3.close()

