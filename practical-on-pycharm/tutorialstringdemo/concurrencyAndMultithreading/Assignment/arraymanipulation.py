import numpy as np

#4X4 arr with 0
arr = np.zeros((4,4), dtype=np.int32)
#print(arr)

#4X4 with diagonal 1
for i in range(len(arr)):
    arr[i][i] = 1
#print(arr)

#Replace last row with random value from 1 to 10
for i in range(len(arr)):
    arr[3][i]=np.random.randint(1,10)

print(arr)

