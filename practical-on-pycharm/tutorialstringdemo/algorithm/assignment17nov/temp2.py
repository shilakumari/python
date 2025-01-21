#Reverse string as "education in Transformation A"
"""
s="A Transformation in education"
l=[]
s1 = ""
for i in range(len(s)):

    if s[i] ==" ":
        l.append(s1)
        s1=""
    else:
        s1 += s[i]
l.append(s1)
#print(l)
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")"""

#check palindrome string
"""s="naman"
s1=""
for i in range(len(s)-1,-1,-1):
    s1 += s[i]
if s==s1:
    print("Yes")
else:
    print("No")

#Find factorial of a number
n=5
fact=1
for i in range(n,0,-1):
    fact *= i
print(fact)

#remove duplicate from list
l=[1, 2, 2, 3, 4, 4, 5]
set1=set(l)
print(set1)"""

#Reverse string and maintain relative order of the sting
#"hi    there"- "ih    ereht"
s="hi   there"
l=list(s)
rs=""
i=0
while i<len(l):
    count=0
    if l[i]==" ":
        rs += l[i]
        i += 1
    else:
        while i<len(l) and l[i]!=" ":
            count+=1
            i+=1
        for k in range(count):
            rs += l[i-1-k]
print(rs)