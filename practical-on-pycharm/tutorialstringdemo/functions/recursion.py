def factorial(n):
    if n==1:
        result= 1
    else:
        result= n*factorial(n-1)
    return result
print(factorial(5))
