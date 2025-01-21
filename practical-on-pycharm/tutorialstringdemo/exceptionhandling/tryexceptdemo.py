import logging
#log will stored in mylog.log
logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

try:
    a,b = [int(x) for x in input("Enter two numbers").split()]
    logging.info("Division in progress")
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("Division by zero")
print("Code after the execution")