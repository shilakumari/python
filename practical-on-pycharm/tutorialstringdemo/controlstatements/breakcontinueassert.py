#break uses to terminate the loop when condition matched
#Break the loop if 5 is present
lst=[3, 6, 7, 5, 9, 10]
for i in lst:
    if i==5:
        break
    print(i)
print("\n")

#continue will continue the execution of loop after skipping the condition
#Print from 1 to 20 and skip multiples of 3
#Using for loop
"""for i in range(1,21):
    if i%3==0:
        continue
    print(i)
"""
#Using while loop
x=0
while x<20:
    x+=1
    if x%3==0:
        continue
    print(x)

#assert x>10
i=int(input("Enter a number greater than 10"))
assert i>10, "Wrong number entered"
print("I entered",i)

