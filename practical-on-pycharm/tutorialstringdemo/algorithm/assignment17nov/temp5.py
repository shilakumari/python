n=5
arr=[14,7,8,2,4]
sum =0
minIndex=-1
for i in range(len(arr)):
    sum += arr[i]
for i in range(len(arr)):
    if (sum-arr[i]) %7 == 0 :
        if minIndex ==-1:
            minIndex =i
        else :
            if arr[i] < arr[minIndex] :
                minIndex =i
print(minIndex )
