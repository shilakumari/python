"""try:
    print(x)
except ValueError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
#Something else went wrong
"""
"""
try:
    print("")
    try:
        print(2/0)
    except ZeroDivisionError:
        print("Divide by zero s not valid")
except ValueError:
    print("Variable c is not defined")
except:
    print("Something else went wrong")
#o/p: Divide by zero s not valid
"""
"""
try:
    f=open("hello.txt","w")
    try:
        f.write("I am writing")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening to the file")

f1=open("hello.txt","r")
data=f1.read()
print(data)
f1.close()
"""

"""x=-1
if x<0:
    raise Exception("Sorry, no numbers below zero")
#o/p:Exception: Sorry, no numbers below zero
"""

class NegativeDivisionFault(Exception):
    #Exception raised for custom error in the application.
    def __init__(self,message,error_code):
        super().__init__(message)
        self.error_code=error_code
    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

def divide(a,b):
    if b<0:
        raise NegativeDivisionFault("Division by zero is not allowed",100)
    return a/b

#d = divide(5,-1)
#print(d)
#o/p:
#raise NegativeDivisionFault("Division by zero is not allowed",100)
#NegativeDivisionFault: <exception str() failed>

d = divide(5,0)
print(d)
#o/p:
#ZeroDivisionError: division by zero