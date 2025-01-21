class Student:
    def __init__(self,id, name, testscore):
        self.id=id
        self.name=name
        self.testscore=testscore
    def display_student(self):
        print(self.id,self.name,self.testscore)
        