import csv
with open(r"notes.txt","r") as f:#r mean relative path
	reader = csv.reader(f)
	for row in reader:
		print(row)
#o/p:
#['Hello World']
#['i got it']
#['Thank you everyone']

with open("csv-file.csv","r") as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)
#o/p:
	['1', '2', '3']
	['4', '5', '6']