import csv
with open("employees.csv","r") as f:
    lines = csv.reader(f)
    for line in lines:
        print(line)

data="Diana,Data Scientist,75000"
with open("employees.csv","a") as f:
    f.write(data)

print()
with open("employees.csv","r") as f:
    lines = csv.reader(f)
    for line in lines:
        print(line)

