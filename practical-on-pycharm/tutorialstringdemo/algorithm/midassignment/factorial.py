n=6 #6*5*4*3*2*1 = 720
fact = 1
if n==1:
    fact = 1
else:
    for i in range(n,0,-1):
        fact *= i
print(fact)



