def reverse(itr):
    pos = len(itr)-1
    if type(itr)==list:
        rev = []
    else:
        rev = ''
    for i in range(pos,-1,-1):
        if type(itr)==list:
            rev.append(itr[i])
        else:
            rev += itr[i]
    return rev

print(reverse([1,2,3,4,5]))
print(reverse("hello"))
