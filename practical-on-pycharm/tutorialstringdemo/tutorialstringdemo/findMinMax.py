def findMinMax(arr):

    minimum = arr[0]

    i=1

    while i != len(arr):
        if minimum > arr[i]:
            minimum = arr[i]
        i += 1

    return minimum

print(findMinMax([15, 2, 34, 8, 19]))

