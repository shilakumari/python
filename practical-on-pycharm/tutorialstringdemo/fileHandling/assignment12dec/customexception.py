class NegativeNumberError(Exception):
    pass

def check_positive(num):
    try:
        if num < 0:
            raise NegativeNumberError
        else:
            print(f"Number: {num}")
    except NegativeNumberError:
        print("Negative numbers are not allowed!")

n=5
check_positive(n)

#Input: 5
#Output: Number: 5

#Input: -3
#output: Negative numbers are not allowed!
