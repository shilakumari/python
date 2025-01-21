"""try:
	int("hi")
except ValueError:
	print("Valerr")
except Exception:
	print("Other err")
#o/p:Valerr


try:
	int("hi")
except Exception:
	print("Valerr")
except ValueError:
	print("Other err")
#o/p:Valerr
"""

def check_age(age):
    if age<0:
        raise ValueError("Age cannot be negative!")
    return f"Your age is: {age}"

try:
    print(check_age(-5))
except ValueError as e:
    print(e)
#o/p: Age cannot be negative!