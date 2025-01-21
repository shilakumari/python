#field names
import csv

fields=["Name","Branch","Year","CGPA"]

#Data rows of csv file
rows=[["Nikhil","COE","2","9.0"],["Naresh","COE","3","9.0"],["Aditya","IT","1","9.3"],["Sahil","EP","2","9.0"]]

#name of csv file
filename="university_records.csv"

#writing to csv file
with open(filename,"w") as csvfile:
    #creating a csv writer object
    csvwriter=csv.writer(csvfile)

    #writing the fields
    csvwriter.writerow(fields)

    #writing the data rows
    csvwriter.writerows(rows)

#reading using csv.reader()
with open(filename,mode="r") as file:
    csvfile = csv.reader(file)
    for line in csvfile:
        print(line)