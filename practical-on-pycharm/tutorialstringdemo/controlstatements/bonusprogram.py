#Employee name and salary input from the user
#Find employee salary by employee's name
from random import choice

n=int(input("Enter the number of employee"))
employee={}

for i in range(n):
    name=input("Enter employee name")
    salary=int(input("Enter employee salary"))
    employee[name]=salary

#Print Employee
keys=employee.keys()
for each_key in keys:
    print("Name:",each_key,"Salary:",employee[each_key])

while True:
    name=input("Enter employee name")
    salary=employee.get(name,-1)
    if salary==-1:
        print("Employee is does not exits")
    else:
        print("Salary of employee", salary)
    choice=input("Do you want to check for another employee[Yes|No]")
    if choice=='No':
        break
