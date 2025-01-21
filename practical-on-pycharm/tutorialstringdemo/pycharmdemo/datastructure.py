students={"John":["Python","Django","DRF"],"Bob":["Java","Spring"],"Jim":["js","node","react"]}
key=students.keys()
for eachKey in key:
    print("Courses taken by ",eachKey," are:")
    for eachCourse in students[eachKey]:
        print(eachCourse)