def findGCD(a, b):
    result = 0
    if a<b:
        for i in range(1, a+1):
            if a%i==0 and b%i==0:
                result = i
    else:
        for i in range(1, b+1):
            if a%i==0 and b%i==0:
                result = i
    return result
print(findGCD(36, 48))


