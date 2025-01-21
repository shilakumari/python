import pickle,studenttodump

#wb because serializing object into a file
f=open("student.dat","wb")
s=studenttodump.Student(123,"John",90)

pickle.dump(s,f)
f.close()

