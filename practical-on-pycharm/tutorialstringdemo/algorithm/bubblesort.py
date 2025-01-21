"""
Bubble Sort: To sort list
	1. Input is list
	2. Output we want is sorted list
	3. Compare two elements to sort from left to right
	4. if two element are already sorted, then move to next pair
	5. if two element are not sorted, then swap
	6. repeat previous three steps till we reach end of the list
	7. now last element is fixed, so repeat previous four steps for list except last element

"""
l=[12,2,54,4,100]
n=len(l)
for i in range(n):
    print(i)
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

print(l)


