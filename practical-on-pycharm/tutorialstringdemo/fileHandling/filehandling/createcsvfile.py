f1=open("csv-file.csv","w")
print(f1.write("1,2,3\n"))#6, print return number of lines those are adding
f1.write("4,5,6\n")
f1.close()
#o/p:
#1,2,3
#4,5,6