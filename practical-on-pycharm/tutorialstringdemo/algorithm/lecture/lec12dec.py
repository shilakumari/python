"""try:
    numerator=int(input("Enter numerator:"))
    denominator=int(input("Enter denominator"))
    result=numerator/denominator
    print("Result:",result)
except:
    print("An error occurred.")
"""

"""try:
    file=open('data.txt','r')
    data=file.read()
    number=int(data)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Could not convert data to an integer.")
"""

"""try:
    #f=open("abc.txt")
    a=3/0
except FileNotFoundError:
    print("file not there")
except:
    print(2)
"""
#To create the file
"""f=open("hello.txt","w")
f.write("hello\n")
f.close()


try:
    f=open("hello.txt")
    a=int("hi")
except (FileNotFoundError,ValueError):
    print("file not there or value error")
#o/p:file not there or value error (because of line, a=int("hi"))
"""

"""try:
    n=int(input("Enter a number:"))
except ValueError:
    print("That's not a valid number!")
else:
    print("You entered:",n)
"""
#o/p:Enter a number:12
#You entered: 12

age=int(input("Enter your age:"))
if age<0:
    raise ValueError("Age cannot be negative!")
else:
    print("Your age is:",age)
#o/p:
#Enter your age:23
#Your age is: 23
