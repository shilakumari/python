"""n=3
for i in range(1, n+1):
    num = int(input())
    for j in range(1,num+1):
        if num%j==0:
            print(j,end=' ')
    print()"""
"""30  35  25
    30  35  40
    30  35  35
    30  25  35
    """
"""n=3
for i in range(1, n+1):
    a, b, c = (input("Enter input by separated by space")).split()
    print(a, b, c)
    if a<=b and c<=b:
        print("Ac")
    else:
        print("No Ac")"""

#find dominant digit
#29- 9, 544- 5
"""num=29
highestDigit=0
while num > 0:
    r=num%10
    print(r)
    if r > highestDigit:
        highestDigit=r
    num = num//10

print("max", highestDigit)"""

"""st="abcde"
n=5
for i in range(n-1,-1, -1):
    print(st[i])
for i in range(0,n,2):
    print(st[i])"""

"""str1="Samantha examined the letter and found it contained a hidden message."
vowels="AaEeIiOoUu"
spce=" "
c = [c for c in str1 if c not in vowels]
print(c)
consonants = "".join(letter for letter in c if letter.isalpha())
print(consonants)
consonantsCount = len(consonants)
print(consonantsCount)"""

#ASCII value of uppercase alphabets – 65 to 90.
#ASCII value of lowercase alphabets – 97 to 122
#print(chr(65))
#print("B",ord("B"))

#check palindrome string
"""s1 = "Samantha"
s2=s1[-1::-1]
print(s2)
for i in range(len(s1)):
    if s1[i]==s2[i]:
        print("a")
#print(s1.e)

text="abbba"
print(text[::-1])
print(text[::-1]==text)

num=12420
match = "420"
s = str(num)
if match in s:
    print("Caught")
else:
    print("Escape")
"""
"""l = [[1,2,3],[4,5,6],[7, 8, 9]]
def isPrimeNumber(num):
    flag = True
    if num < 2:
        flag = False
    else:
        for i in range(2, (num // 2)+1):
            if num % i == 0:
                flag = False
                break
    return flag

count=0
for i in range(len(l)):
    length = len(l[i])
    for j in range(length):
        if isPrimeNumber(l[i][j]):
            count += 1

print(count)"""

"""for i in l:
    oddAdd=0
    for j in i:
        print(j, end=" ")
        if j%2 != 0:
            oddAdd += j
    print("oddAdd",oddAdd)"""

#print 2D list in ZIG-GAG format
"""for i in range(len(l)):
    sizeOfI = len(l[i])
    if i%2 != 0:
        for j in range(sizeOfI):
            print(l[i][j], end=" ")
    else:
        for j in range(sizeOfI-1,-1,-1):
            print(l[i][j], end=" ")"""

#sum of first and last column
l = [[1,2,3],[4,5,6],[7, 8, 9]]
n=3
m=3
for i in range(n):
    addition = 0
    for j in range(m):
        if i==0 or i==(m-1):
            addition += l[j][i]
    if addition > 0:
        print(addition)

