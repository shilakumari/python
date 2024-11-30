try:
    #first argument for filename, second for mode(read or write)
    #w for write mode
    f = open("myfile","w")
    a,b = [int(x) for x in input("Enter two numbers").split()]
    c = a/b
    f.write("Writing %d into file"%c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter non zero numbers")
finally:
    f.close()
    print("File closed")
print("Code after the exception")
