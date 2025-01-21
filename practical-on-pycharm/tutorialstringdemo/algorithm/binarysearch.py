l1 = [0, 7, 10, 14, 45, 47]
t1 = 47
"""
    #Algorithm
    1. Input: sorted list e.g. [1,3,6,9,5]
    2. Input: also has target t
    3. pick the middle element of list m
    4. if m is same as t, output index of m
    5. if m is greater than t,
    then repeat entire algorithm for list on the left of m
    6. if m is less than t, 
    then repeat entire algorithm for list on the right of m
"""


def binary_search(l1, t1):
    low = 0
    high = len(l1) - 1

    while (low <= high):
        mid = (low + high) // 2
        if l1[mid] == t1:
            return mid
        elif l1[mid] > t1:
            high = mid - 1

        else:
            low = mid + 1
    return -1

print(binary_search(l1, t1))  # 4