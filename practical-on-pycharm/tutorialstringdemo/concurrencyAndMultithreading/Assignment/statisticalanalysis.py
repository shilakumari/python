import numpy as np

arr=np.random.randint(1,100, size=1000)
print(arr)

#mean value - total element/number of elements
mean_val=np.mean(arr)
print("Mean Value: ",mean_val)

#Median value - middle value in sorted data
median_val=np.median(arr)
print("Median Value: ",median_val)

#Standard deviation
std_val=np.std(arr)
print("Standard Deviation: ",std_val)