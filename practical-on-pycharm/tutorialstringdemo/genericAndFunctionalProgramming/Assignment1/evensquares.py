from functools import reduce

def sum_even_squares(numbers: list[int]) -> int:
    # Apply map, filter, and reduce
    even_squares=list(map(lambda x:x**2,(filter(lambda x:x%2==0,numbers))))
    squares_sum=reduce(lambda x,y:x+y,even_squares)
    return squares_sum
# Example usage:
print(sum_even_squares([1, 2, 3, 4]))
# Expected output: 20 (because even squares are 4 (2²) and 16 (4²), sum = 20)
