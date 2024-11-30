#Example1...
list2dimensional = [[1,2,3],[4,5,6],[7,8,9]]
for row in list2dimensional:
    for element in row:
        print(element,end=' ')
print()

#Example2...
l2d = [[1,2],[3,4],[5,6]]
for i in range(len(l2d)):
    for j in range(len(l2d[i])):
        if i==j:
            print(l2d[i][j], end=' ')
print()

#In cube, first dimension for table, second for row, third for element
cube=[[[1,2], [3,4]], [[5,6], [7,8]]]
print(cube[0][1][1])#4
for table in cube:
    for row in table:
        for ele in row:
            if ele%2==0:
                print(ele,end=' ')#2 4 8 6
print()

cube[0][1].pop(0)# Removing 3
print(cube)

matrix1 = [[1,2],[3,4],[5,6]]
matrix1[1].append(7)
matrix1[2].pop(0)# removing 5
print(matrix1)

# Way 1
matrix2 = [[i for i in range(3)] for j in range(3)]
print(matrix2)

#Way 2
matrix3=[]
for j in range(3):
    matrix3.append([])
    for i in range(3):
        matrix3[j].append(i)
print(matrix3)

