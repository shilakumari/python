class Course:

    #parameterized constructor
    def __init__(self, name, ratings):
        self.name=name
        self.ratings=ratings

    #Instance method for average rating
    def average(self):
        numberOfRatings = len(self.ratings)
        avg = sum(self.ratings)/numberOfRatings
        print("Average rating for",self.name,"is",avg)

c1=Course("Java Course",[3, 4, 4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2=Course("Java Web Services",[5, 5, 5, 5])
print(c2.name)
print(c2.ratings)
c2.average()
