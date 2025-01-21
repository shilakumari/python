def bmiusecase(height,weight):
    heightinmeters=height*0.4536
    bmi = weight / (heightinmeters * heightinmeters)
    return bmi

print(bmiusecase(5.6,70))
print(bmiusecase(6.2,100))
print(bmiusecase(5.2,58))
print(bmiusecase(5.8,70))