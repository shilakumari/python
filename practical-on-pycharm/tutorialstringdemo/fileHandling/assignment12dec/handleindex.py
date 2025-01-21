l=[1,2,3,4,5]
index_by_user=int(input())

try:
    print(f"Element at index {index_by_user} is: {l[index_by_user]}")
except IndexError:
    print("Index out of range")