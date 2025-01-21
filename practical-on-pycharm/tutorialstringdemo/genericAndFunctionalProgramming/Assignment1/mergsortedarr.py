from typing import List, TypeVar

T = TypeVar('T')

def merge_sorted_lists(a: List[T], b: List[T]) -> List[T]:
    # Merge the two sorted lists a and b into a single sorted list
    return list(sorted([*a,*b]))

# Example usage:
print(merge_sorted_lists([1,3,5], [2,4,6]))
# Expected output: [1,2,3,4,5,6]
