import random

#dice1=random.randint(1,6)
#dice2=random.randint(1,6)
#random.seed(20)
dict1=dict()
for i in range(100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum_dices = (dice1+dice2)

    if sum_dices not in dict1.keys():
        dict1[sum_dices] = 1
    else:
        dict1[sum_dices] += 1

for key,value in dict1.items():
    print(f"Sum: {key} and their frequency: {value}")
