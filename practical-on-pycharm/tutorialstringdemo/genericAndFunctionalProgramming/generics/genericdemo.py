from typing import List
nums: List[int]=[1,2,3]
print(type(nums))
print(nums[0])
print(nums[1])
print(nums[2])

#To check the size
import sys
print(sys.getsizeof(nums))#88
l1=[1,2,3]
print(sys.getsizeof(l1))#88

