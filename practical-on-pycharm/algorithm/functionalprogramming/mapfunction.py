nums = [1,2,3,4]
squares  = list(map(lambda x:x*x,nums))
print(squares)#[1, 4, 9, 16]

"""def sq(x):
    return x*x
squares  = list(map((x*x for x in nums),nums))
print(squares)#[1, 4, 9, 16]"""