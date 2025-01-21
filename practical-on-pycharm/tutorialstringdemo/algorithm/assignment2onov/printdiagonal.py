def print_diagonals(matrix, r, c, k):
    for i in range(r):
        for j in range(c):
            if k == matrix[i][j]:
                # print(matrix[i][j])
                i1 = i
                j1 = j
                # Upper left
                while i1 >= 0 or j1 >= 0:
                    i1 -= 1
                    j1 -= 1
                    print(matrix[i1][j1], end=" ")
                # Upper right
                """while i1 >= 0 and j1 < c:
                    i1 -= 1
                    j1 += 1
                    print(matrix[i1][j1], end=" ")
                # Lower left
                while i1 < r and j1 >= 0:
                    i1 += 1
                    j1 -= 1
                    print(matrix[i1][j1], end=" ")
                # Lower right
                while i1 < r and j1 < c:
                    i1 += 1
                    j1 += 1
                    print(matrix[i1][j1], end=" ")"""

matrix=[[1,2,3],[4,5,6],[7,8,9]]
r=3
c=3
k=6
print_diagonals(matrix, r, c, k)