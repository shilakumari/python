import pickle

f=open("student.dat","rb")
obj=pickle.load(f)
#calling student object method
obj.display_student()
