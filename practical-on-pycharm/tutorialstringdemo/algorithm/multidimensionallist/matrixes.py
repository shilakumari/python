"""matrix1=[[1,2],[3,4],[5,6]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if i==j:print(matrix1[i][j],end=" ")#1 4
"""

"""cube=[[[1,2], [3,4]], [[5,6], [7,8]]]
print(cube[0])#[[1, 2], [3, 4]]
print(cube[0][1].pop(0))#3 - removed 3 from the 3D list
print(cube)#[[[1, 2], [4]], [[5, 6], [7, 8]]]

cube1=[[[1,2,3]],[[4,5]],[[6,7,8,9]]]
for table in cube1:
    for row in table:
        for elem in row:
            if elem%2==0:
                print(elem,end=" ")#2 4 6 8
print()
"""

#List comprehension
#matrix2=[[i+j for i in range(2)]for j in range(2)]
#print(matrix2)#[[0,1],[1,2]]

#4D matrix
"""matrix3=[[0],[[1,2]], [[[3,4],5]]]
print(matrix3[0][0])#0
print(matrix3[1][0][0])#1
print(matrix3[1][0][1])#2
print(matrix3[2][0][0][1])#4
print(matrix3[2][0][1])#5"""
"""
def multiply(x,y=2):
    return x*y
result=multiply(4)
print(result)#8"""

class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

myCar=Car("Honda","Civic")
print(myCar.make, myCar.model)