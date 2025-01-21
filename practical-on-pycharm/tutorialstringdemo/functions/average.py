"""def average(a,b):
        print("a:",a)
        print("b:",b)
    print("Average of two numbers is: ",(a+b)/2)

#Envoking function
average(10,20)"""

def average(a,b):
    return (a+b)/2
print(average(10,20))
#Keyword arguments
print(average(b=50,a=60))

#Default arguments
def average(a=10, b=20):
    print("a:", a)
    print("b:", b)
    return (a+b)/2
print(average(a=60))