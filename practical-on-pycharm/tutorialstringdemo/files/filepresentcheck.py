import os,sys

if os.path.isfile("myfile.txt"):
    f = open("myfile.txt", "r")
else:
    print("File is not present")
    sys.exit()

s = f.read()
print(s)
f.close()