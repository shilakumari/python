import pickle
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

students = [
    Student("Alice", "A"),
    Student("Bob", "B"),
    Student("Charlie", "A")
]

with open("scores.pkl","wb") as f:
    pickle.dump(students,f)

with open("scores.pkl","rb") as f:
    data = pickle.load(f)
    for d in data:
        print(d)