#s="aabc" #o/p:ab
s="abccdda" #o/p:3
c=0
s1=""
n= len(s)
for i in range(n-1):
    if i%2==0:
        if s[i]!=s[i+1]:
            s1 += s[i]
        else:
            c += 1
            s1 += ""
    else:
        s1 += s[i]
print()
s1 += s[n-1]
n2=len(s1)
s2=""
for i in range(n2-1):
    if i % 2 == 0:
        if s1[i] != s1[i + 1]:
            s2 += s1[i]
        else:
            c += 1
            s2 +=""
    else:
        s2 += s[i]
s2 += s1[-1]
print("s2",s2)



if len(s1)%2!=0:
    c += 1
    print(c)
    print(s1[:n2-1])
else:
    print(c)
    print(s1)

'''
print("hi")
'''