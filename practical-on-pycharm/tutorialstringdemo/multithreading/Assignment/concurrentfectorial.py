
def calculate_factorial(n):
    if n==0 or n==1:
        return  1
    fact=n*calculate_factorial(n-1)
    return fact

