giv_arr=[1,2,1]
giv_subset=[1,2]

def is_subset(arr,subset):
    n = len(arr)
    m = len(subset)
    for i in range(n):
        found=False
        if m==1:
            if subset[0] in arr:
                return  True
        else:
            for j in range(m):
                if arr[i]==subset[j]:
                    found=True
                    break

        if not found:
            return False
    return True


if is_subset(giv_arr,giv_subset):
    print("Yes")
else:
    print("No")

