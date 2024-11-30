#print common elements
"""n=3
a1=[4,5,7]
a2=[9,2,5]
for i in a1:
    for j in a2:
        if i==j:
            print(i,end=" ")
print()"""

#remove vowel followed by constant
#s="deefugvbaaa"
"""s="abcfigu"
l=list(s)
print(l)
vowel="aeiouAEIOU"
s2=""
i=0
while i<len(l)-1:
    count=0
    if l[i] not in vowel:
        s2 += l[i]
        i += 1
    else:
        while i<len(l)-1 and (l[i] in vowel):
            count+=1
            i+=1
        print("count",count,"i,l[i]",i,l[i])
        if l[i] not in vowel:
            for k in range(count):
                s2 += ""
            #print("l",l[i-1-k])
        else:
            for k in range(count):
                s2 += l[i-1-k]
s2 += l[len(l)-1]
print(s2)"""

#Find the equilibrium first occurs in the array
#arr=[15,1,5,5,5]
"""arr=[1,2,3]
n=len(arr)
flag=False
equilibrium=-1
for i in range(1,n-1):
    ls=0
    rs=0
    for j in range(i):
        ls += arr[j]
    for k in range(i,n):
        if k==i:
            continue
        else:
            rs += arr[k]
    if ls==rs:
        flag=True
        print("ls",ls,"rs",rs)
        #print(i)
        equilibrium=i
        break
print(equilibrium)"""

n=4
codingX= 0
days=["SSSSEEEECCCCEECCCC","CCCCCSSSSEEECCCCSS","SSSSSEEESSCCCCCCCS",
    "EESSSSCCCCCCSSEEEE"]
maximum=0
for i in range(n):
    count=0
    count1=0
    n2=len(days[i])
    s1=days[i]
    #print(s1)
    for j in range(n2):
        if s1[j]=="C":
            count += 1
        else:
            if count>count1:
                count1=count
            count = 0
    if maximum<count1:
        maximum=count1
    print(i,count1)
print("maximum",maximum)

#********
"""n2=4
days2=["SSSSEEEECCCCEECCCC","CCCCCSSSSEEECCCCSS","SSSSSEEESSCCCCCCCS",
    "EESSSSCCCCCCSSEEEE"]
isLastC=False
maxC=0
for i in range(1, n):
    c=0
    s1=days2[i-1]
    s2=days2[i]
    length = len(s1)-1
    length2= len(s2)-1
    if s1[length-1]=="C":
        isLastC=True
        while length>=0 and s1[length]=="C":
            c += 1
            length -= 1"""



