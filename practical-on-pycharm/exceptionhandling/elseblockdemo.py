try:
    f = open("myfile","w")
    a,b = [int(x) for x in input("Enter two numbers").split()]
    c = a/b
    f.write("Writing %d into file"%c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter non zero numbers")
#If no exception then else-block executes
else:
    print("You have entered non zero numbers")
finally:
    f.close()
    print("File closed")
print("Code after the exception")
