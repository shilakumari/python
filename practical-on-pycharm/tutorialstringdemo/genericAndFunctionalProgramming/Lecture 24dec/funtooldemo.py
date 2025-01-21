from functools import reduce
nums=[1,2,3,4,5]
result = reduce(lambda x,y: x*y, nums)
print(result)#120

nums2=[10,20,4,45,99]
result=reduce(lambda x,y:x if x>y else y,nums2)
print(result)#99