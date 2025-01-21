import numpy as np
import random

from numpy.ma.core import multiply

matrix1=np.random.randint(1, 10, size=(3,3))
print(matrix1)

matrix2=np.random.randint(1, 10, size=(3,3))
print(matrix2)

#Addition of matrices
addition = np.add(matrix1,matrix2)
print("Addition: \n",addition)

#Multiplication of matrices (not element wise)
multiplication = np.dot(matrix1,matrix2)
print("Multiplication: \n",multiplication)

#Multiplication of matrices (element wise)
multiplication_elementwise = matrix1*matrix2
print("Multiplication: \n",multiplication_elementwise)