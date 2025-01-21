a,b=input().split()
try:
    ai=int(a)
    bi=int(b)
    print(f"Result: {ai/bi}")
except ValueError:
    print("Invalid input! Please enter numbers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

#10 2
#Result: 5.0

#10 zero
#Invalid input! Please enter numbers.

#10 0
#Division by zero is not allowed.