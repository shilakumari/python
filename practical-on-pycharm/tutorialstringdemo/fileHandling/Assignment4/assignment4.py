import csv
path=r"C:\Users\Java\PycharmProjects\pycharmdemo\fileHandling\Assignment3\employees.csv"
l=[]
with open(path,"r") as f:
    reader = csv.reader(f)
    for line in reader:
        l.append(line)
    print(l)

for i in range(1,len(l)):
    val=l[i][2]
    if int(val) > 70000:
        print(f"Name: {l[i][0]}, Position: {l[i][1]}")