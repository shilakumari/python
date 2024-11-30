print("Hello World")

"""
#Calculate the sum of digits of a given number
num = 1234
sumOfDigit = 0
while num>0:
    digit = num%10
    print(digit)
    sumOfDigit += digit
    num //= 10
print("Sum of digit", sumOfDigit)

num=5
for i in range(1, num+1):
    for j in range(1, num+1):
        print(j, end=' ')
    print()

num1=3
n=0
for i in range(1, num1+1):
    for j in range(1, num1+1):
        n += 1
        print(n, end=' ')
    print()"""
"""
num2=5
for i in range(1,num2+1):
    for j in range(i):
        print("*", end=' ')
    print()"""
"""
for i in range(1, 6):
    for j in range(1, 6):
        if j==1 or (i==1 or i==5):
            print("*", end=' ')
    print()

n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i!=n and (1<j<n):
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print()"""
"""
rows=5
n = 0
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        n += 1
        print("* ", end="")
    for k in range(i,rows, +1):
        n += 1
        print("#", end=" ")
    print()"""
"""
rows=5
n = 0
for i in range(rows, 0, -1):
    r = rows-i
    for j in range(1, i+1):
        n += 1
        print("* ", end='')
    while r>0:
        n+=1
        print("# ",end='')
        r -= 1
    print()
print(n)

print(5**2//3)

l=[1, 2, 3]
l.insert(1, 4)
print(l)
print(len("Hello World"))
print(bool(0))
print(len("hi"))

x = 5
y = 10
print(x > y or x == 5)
for i in range(3):
    for j in range(i):
        print(i*j, end="")"""
arr=[-11,-2,-31,-41,-5]
maximum = arr[0]
for i in arr:
    if maximum < i:
        maximum = i
print(maximum)


