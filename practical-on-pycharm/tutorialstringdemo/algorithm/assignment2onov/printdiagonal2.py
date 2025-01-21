def print_diagonals(matrix, r, c, k):
    for i in range(r):
        for j in range(c):
            if k == matrix[i][j]:
                i1 = i
                j1 = j
                break
    print(i1,j1)
    count = i1
    while count >0:
            # Upper left
            print(matrix[i1-count][j1-count], end=" ")
            count -= 1
    print(k,end=" ")
    for i in range(i1+1,r):
        for j in range(j1+1,c):
           # Lower Right
           count = 1;
           if i == i1 + count and j == j1 + count:
              print(matrix[i][j], end=" ")
              count += 1
    print("")
    for i in range(i1-1,-1,-1):
        for j in range(j1+1,c):
           # Upper right
           count = 1
           #print(i,j,count)
           if i == i1 - count and j == j1 + count:
              print(matrix[i][j], end=" ")
              count += 1
    print(k,end=" ")
    for i in range(i1+1,r):
        for j in range(j1):
           # Lower left
           count = 1
           if i == i1 + count and j == j1 - count:
              print(matrix[i][j], end=" ")
              count += 1

matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
r=3
c=3
k=13
print_diagonals(matrix, r, c, k)
print("end")