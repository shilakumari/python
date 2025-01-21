#output all the integers separated in
#the array from left to right that are not smaller than those on its right side.
n=6
m=[16, 17, 4, 3, 5, 2]

for i in range(n):
    flag = True
    for j in range(i + 1, n):
        if m[i] < m[j]:
            flag=False
            break
    if flag:
        print(m[i],end=" ")
    #flag