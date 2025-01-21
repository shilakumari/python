a,b=map(int,input().split())
try:
    print(f"{a/b}")
except ZeroDivisionError:
    print("Division by zero is not allowed")