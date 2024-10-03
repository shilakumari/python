#Display numbers from 50 to 70

for i in range(50,71):
    print(i)

for i in range(50,70,3):
    print(i)

#Print product in a list
lst=[1,2,3,4,5]
prod=1
for i in lst:
    prod*=i
print("Product is",prod)

#Generate a table for a given number
n=int(input("Enter a number for generating a table"))
for i in range(1,11):
    print(n,"X",i," = ",n*i)
