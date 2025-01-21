nums=[8, 6, 7, 4, 10, 8]
n=len(nums)
ans= [nums[0]]
for i in range(1, n):
    if nums[i] > ans[-1]:
        ans.append(nums[i])
        print(ans)
    else:
        low = 0
        high = len(ans) - 1
        while low < high:
            mid = (low + high) // 2
            if ans[mid] < nums[i]:
                low = mid + 1
            else:
                high = mid
        ans[low] = nums[i]
        print(ans)
print(len(ans))


"""max1 = 1
  len1 = 1
  maxindex = 0
  for i in range(1, n):
    if arr[i] > arr[i - 1]:
        len1 += 1
    else:
        if max1 < len1:
            max1 = len1
            maxindex = i - max1
        len1 = 1

    if i == n - 1 and max1 < len1:
        max1 = len1
        maxindex = n - max1
  print(max1 + maxindex)"""

"""max_ele=-1
sec_max=-1
l=[]
length=0
for k in range(len(arr)-1):
    for i in range(len(arr)-1):
        if max_ele == -1:
            if arr[i]<arr[i+1]:
                max_ele=arr[i]
                print(max_ele)
                l.append(max_ele)
        elif arr[i]==sec_max:
            continue
        elif max_ele<arr[i]:
            max_ele = arr[i]
            print(max_ele)
            l.append(max_ele)
    sec_max=max_ele
    if length<len(l):
        length=len(l)
    l=[]
    max_ele=-1

print("length",length)
"""
