#s="abcfigu"
s="eaimftvouih"
vowel="aeiouAEIOU"
s2=""
for i in range(len(s)-1):
    if s[i] in vowel:
        if (s[i+1] not in vowel) and (s[i+1].isalpha()):
            continue
        else:
            s2 += s[i]
    else:
        s2 += s[i]

s2 += s[len(s)-1]

print(s2)


#find largest value in list
#def findlargest(l):
#    for value in l:

#arr=[1,2,3,4],output: N=4,M=2
#arr=[1,2,3,4]
"""arr=[5, 0, 9, 7, 20]
flag=False
for i in range(len(arr)-1, -1,-1):
    N1 = arr[i]
    for j in range(len(arr)):
        M1 = arr[j]
        if N1 == M1:
            continue
        if N1 == M1*2:
            flag=True
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")"""

#If array element is less than 3 then make it -1.
"""arr=[1,3,2]
maximum = arr[0]
for i in range(1,len(arr)):
    if maximum < arr[i]:
        maximum=arr[i]
print(maximum)
for i in arr:
    if i < maximum:
        i = -1
    print(i,end=" ")
print()"""

"""arr=[3,0,6,2,7]
k=9
count = 0
for i in range(len(arr)):
    print("i",i)
    for j in range(i+1,len(arr)):
        print("j",j)
        if i==j:
            continue
        if arr[i]+arr[j] == k:
            #print("i",arr[i],"j",arr[j])
            count += 1
print(count)"""

#find out the count of elements those are greater than its neighbour
"""arr=[8,0,-2,1,-4]
count = 0
if len(arr)<3:
    if arr[0] < arr[len(arr)-1]:
        count += 1
else:
    for i in range(1,len(arr)-1):
        if (arr[i]>= arr[i-1]) and (arr[i]>= arr[i+1]):
            count += 1
            print(arr[i])
    if (arr[0]>arr[1]) and (arr[0]>arr[len(arr)-1]):
        count += 1
    if (arr[len(arr)-1]>arr[len(arr)-2]) and (arr[len(arr)-1]>arr[0]):
        count += 1
print(count)

s="aaabbbbcc"
c = s[0]
count=0

for i in range(len(s)):
    #print("i",i)
    if c==s[i]:
        count += 1
    else:
       print(c+str(count), end="")
       c = s[i]
       count=1
print(c+str(count),end="")

#Ternary operator
n=80
s= "Even" if n%2==0 else "Odd"
print(s)"""

#count contiguous(start and last char are same) substring
#aba=a,b,a,aba
"""s="aba"
count=0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i]==s[j]:
            count += 1

print(count)"""

#Make the even "A"
"""s="ATAAGACC"

c="A"
count=0
for i in range(len(s)):
    c1=s[i]
    if c==s[i]:
        count += 1
    else:
        if c=="A":
            #print(c+str(count), end="")
            if count%2!=0:
                print(c+(c*count), end="")
            else:
                print(c*count,end="")
        else:
            print(c*count, end="")
        c = s[i]
        count=1
if c=="A":
    if count % 2 != 0:
        print(c+(c*count), end="")
    else:
        print(c * count, end="")
else:
    print(c*count, end="")
#print(c+str(count),end="")
"""

text = "hello-world-python"
parts = text.split("-", 1)#['hello', 'world-python']
result="-".join(parts[::-1])
print(result)#world-python-hello

x="10"
if isinstance(x,int) or type(x)==int:
    print("It's an integer")
else:
    print("It's not an integer")
#o/p: It's not an integer