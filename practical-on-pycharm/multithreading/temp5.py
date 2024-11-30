#print W shape
"""n=1
for i  in range(1,n+1):
    #1st V shape
    for j in range(1, n+1):
        if j==i:
            print("\\",end="")
        else:
            print(" ", end="")
    for k in range(n,-i,-1):
        #if k > i and i!= n:
        if k > i != n:
            print(" ", end="")
        if k==1:
            print("/",end="")
    #2nd V shape
    for j in range(1, n + 1):
        #if (j<i and i!=1):
        if j < i != 1:
            print(" ", end="")
        if j == i:
            print("\\", end="")
        else:
            print(" ", end="")
    for k in range(n, -i, -1):
        if k > i != n:
            print(" ", end="")
        if k == 1:
            print("/", end="")

    print()"""

"""n=4
for i in range(1, n+1):
    for j in range((n-i+1),0,-1):
        print("*", end="")
        if j>1:
            print(" ",end="")
    if i!=1:
        for j in range(1,i):
            print(".",end="")
    print()"""
n=5
for i in range(n, 0, -1):
    for j in range(1,i+1):
        print("*",end='')
        if j!=i:
            print(".",end='')
    for j in range(i, n):
        print("."*2, end='')
       # print("$", end="")

    print()