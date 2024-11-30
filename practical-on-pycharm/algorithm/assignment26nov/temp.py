#arr=[1,2,3,4,2,1,6,5]
#print least 3 value that is "1, 2, 3", if not "Not possible"
#print top 3 value that is "4, 5, 6", if not "Not possible"
#arr=[51,0,0,11,-11,23]
arr=[-4,-7,-2,-11,-2,-8,0,-122,-66,10]
s=set(arr)
l=list(s)
l.sort()
l2=l
#print(l2)
#For least value
minValue = []
index=len(l2)//2
print("index",index)
for i in range(index+1):
    minValue.append(l2[i])
print("minValue",minValue)

#For max value
maxValue = []
for j in range(len(l2)-1,index-1,-1):
    maxValue.append(l2[j])
maxValue.sort()
print("maxValue",maxValue)

count=0
if len(minValue)>=3:
    t=minValue[:3]
    for i in t:
        print(i, end=" ")
    print()
    """for i in minValue:
        print(i,end=" ")
        count += 1
        if count == 3:
            break
    print()"""
else:
    print("Not possible")

if len(maxValue)>=3:
    t=maxValue[-3::]
    for i in t:
        print(i, end=" ")
    print()
    #print(maxValue[-3::])
else:
    print("Not possible")
