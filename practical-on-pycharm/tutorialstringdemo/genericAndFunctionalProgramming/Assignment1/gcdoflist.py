from functools import reduce

def gcd(a: int, b: int) -> int:
    # Implement the GCD of two integers
    gd=1
    for i in range(1, a+b):
        if a%i==0 and b%i==0:
            gd=i

    return gd


def list_gcd(numbers: list[int]) -> int:
    gcd_of_list = reduce(gcd,numbers)
    return gcd_of_list
# Example usage:
print(list_gcd([8, 12, 16]))
# Expected output: 4
