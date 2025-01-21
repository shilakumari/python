from typing import List, TypeVar

T = TypeVar('T')

def linear_search(arr: List[T], target: T) -> int:
    # Implement linear search logic here
    for data in arr:
        if target==data:
            return 1
    return -1


# Example usage:
print(linear_search([10, 20, 30], 30))  # Expected output: 1
print(linear_search(["apple", "banana", "cherry"], "banana"))  # Expected output: 1
print(linear_search([1.1, 2.2, 3.3], 4.4))  # Expected output: -1
