class Student:
    #static field
    major='CSE'

    def __init__(self, rollno, name):
        self.rollno=rollno
        self.name=name

s1 = Student(101,"Shila")
print("Name",s1.name,"Roll no",s1.rollno,"Major",s1.major)
print(Student.major)

s2 = Student(102,"Vinay")
print("Name",s2.name,"Roll no",s2.rollno,"Major",s2.major)
print(Student.major)
