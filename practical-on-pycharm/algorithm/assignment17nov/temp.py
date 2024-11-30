"""t=(10,20,30,40)
maximum=t[0]
for i in range(1,len(t)):
    if maximum<t[i]:
        maximum = t[i]

print(type(t))
print(maximum)

l=[1,2,2,3,4,4,5]
print(type(l))
s=set(l)
print(type(s))
print(s)

N=3
print(chr(97))
for i in range(N):
    print(chr(i+97),"-",i+1)

n=26
N = 30
for i in range(n):
    c=chr(i+97)
    print(f"{c}-{N+i}")"""

arr1=[1,2,3,4]
arr2=[1,2,3,4,5]
arr3=arr1+arr2
ts=set(arr3)

ls=list(ts)
ls.sort()

for i in ls:
    print(i,end=" ")
print()