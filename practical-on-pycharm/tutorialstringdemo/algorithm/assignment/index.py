#If value present then return index, if not then "valueError"
def indexs(l,k):
    position = -1
    for i in range(len(l)):
        if l[i] == k:
            position = i
            break
    if position != -1:
        return position
    else:
        return ValueError

print(indexs([1,2,3,4,5],3))

