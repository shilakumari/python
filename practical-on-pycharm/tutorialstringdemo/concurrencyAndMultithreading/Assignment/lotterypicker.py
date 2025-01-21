import  random
random.seed(60)
fifty = []
twelve = []

for i in range(1, 51):
    fifty.append(i)
for i in range(1, 13):
    twelve.append(i)

sample1 = random.sample(fifty,5)
sample2 = random.sample(twelve,2)
print(f"Main Numbers: {fifty}, Special Numbers: {sample1}")
print(f"Main Numbers: {twelve}, Special Numbers: {sample2}")