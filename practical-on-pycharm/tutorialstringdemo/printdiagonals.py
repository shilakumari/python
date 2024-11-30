l1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n,m = 4,4
k=11
#print diagonal of k
row = -1
col = -1
for i in range(n):
    for j in range(m):
        if k == l1[i][j]:
            row = i
            col = j
            break
#print(row, col)

d1Row = row
d1Col = col
# k to upper left corner
while d1Row != 0 and d1Col !=0:
    d1Row -= 1
    d1Col -= 1
#print(d1Row,d1Col)
# print printing diagonal (upper-left to lower-right)
while d1Row != n and d1Col != m:
    print(l1[d1Row][d1Col], end=" ")
    d1Row += 1
    d1Col += 1
print()

d2Row = row
d2Col = col
# k to upper right corner
while d2Col != m-1 and d2Row !=0:
    d2Row -= 1
    d2Col += 1
#print(d2Row, d2Col, l1[d2Row][d2Col])
# print printing diagonal (upper-right to lower-left)
while d2Row != n and d2Col != -1:
    print(l1[d2Row][d2Col], end=" ")
    d2Row += 1
    d2Col -= 1
print()
