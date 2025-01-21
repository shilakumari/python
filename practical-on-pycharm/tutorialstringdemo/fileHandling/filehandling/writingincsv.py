import csv
with open("output.csv","w",newline="") as f:
	writer=csv.writer(f)
	writer.writerow(["Name","Score"])
	writer.writerow(["Alice",90])
#o/p:
#Name,Score
#Alice,90