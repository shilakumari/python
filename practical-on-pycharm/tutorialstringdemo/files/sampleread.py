f=open('sample.txt','r')
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline(3))
f.seek(0)
print(f.readlines())
f.close()
