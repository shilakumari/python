print("Hello world")

"""k=5
m=30
totalCost = 0
#first item is free
item = 1
#second item cost k

while totalCost <= m:
    item += 1
    totalCost += (item-1)*k
    print(totalCost)
    m -= k
#print(totalCost)
print(item)"""

"""n=3
x=2
sum=0
#1+x+(x*x)+(X*x*x)+...n
for i in range(n):
    sum += x**i
print(sum)"""

"""
#Prime number
num=152
isPrime = True
if num <2:
    isPrime = False
else:
    for i in range(2, num//2):
        if num%i==0:
            isPrime = False
            break
if isPrime:
    print("Yes, it is prime")
else:
    print("No, it is not prime")
"""

"""
#Print 'Yes' if number and reverse of number both are prime otherwise 'No'
def Solve(num):

    def reverse(n):
        reverseNum = 0
        while n > 0:
            reverseNum = reverseNum * 10 + n % 10
            n = n // 10
        return reverseNum

    def prime(n):
        flag = True
        if n < 2:
            flag = False
        else:
            for i in range(2, n // 2):
                if n % i == 0:
                    flag = False
                    break
        return flag

    for i in range(num):
        n = int(input())
        r = reverse(n)
        if prime(n) and prime(r):
            print("Yes")
        else:
            print("No")

Solve(2)
"""


n1=1023
reverseNum=0
while n1>0:
    reverseNum = reverseNum*10+n1%10
    n1 = n1 // 10
print(reverseNum)

n1=1023
reverseNum=0
for i in str(n1):
    reverseNum = reverseNum*10+n1%10
    n1 = n1 // 10
print(reverseNum)


"""
i   num     n1      n2      reverseNum
    123     123     1      0
0   123     123     10     0*10+123%10=3
1   123     12      100    3*10+12%10=32
2   123     1       1000   32*10+1%10=321
"""
num = [12, 23]
for i in num:
    print(i)
