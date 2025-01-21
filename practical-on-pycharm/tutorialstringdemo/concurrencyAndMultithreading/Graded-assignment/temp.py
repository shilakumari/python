"""
def m1(arr, n):
    max=1
    len=1
    maxindex=0
    for i in range(1, n):
        if arr[i]>arr[i-1]:
            len+=1
        else:
            if max<len:
                max=len
                maxindex=i-max
            len=1

        if i==n-1 and max<len:
            max=len
            maxindex=n-max
    print(max+maxindex)"""
arr=[8, 6, 7, 4, 10, 8 ]
n=len(arr)
#m1(ar,n1)

max = 1
len = 1
maxindex = 0
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        len += 1
    else:
        if max < len:
            max = len
            maxindex = i - max
        len = 1

    if i == n - 1 and max < len:
        max = len
        maxindex = n - max
print(max + maxindex)