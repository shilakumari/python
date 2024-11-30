def contains(l, k):
    flag = False
    for i in l:
        if i == k:
            flag = True
    return flag

print(contains([1,2,3,4,5],3))#True

