import numpy as np

val=np.arange(1, 26)

#subtract 10 which is greater than 15
val_lesser = val[val<=15]
val_greater  = val[val>15]-10

temp_arr=np.concatenate((val_lesser,val_greater))
#print(temp_arr)

final_arr = np.reshape(temp_arr,(5,5))
print(final_arr)
