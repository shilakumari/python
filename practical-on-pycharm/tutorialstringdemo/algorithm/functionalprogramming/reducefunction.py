from functools import reduce

nums=[1,2,3,4]
product=reduce(lambda x,y:x+y,nums)
print(product)#10
multiple=reduce(lambda x,y:x*y,nums)
print(multiple)#24
exponential=reduce(lambda x,y:x**y,nums)
print(exponential)#1
