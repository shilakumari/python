from assignment17nov.temp2 import count

a=[1,1,1,1,1,2,2,2,2,2,3]
key=1
#o/p: 0 3 4
foundAt=-1
firstOccurs=-1
lastOccurs=-1
countOfKey=0
low=0
high=len(a)-1
l=[]
isFound=False
while low<=high and countOfKey<len(a):
    print(low,high)
    mid=(low+high)//2
    if a[mid]==key:
        isFound=True 
        foundAt = mid
        mid = foundAt
        print("low",low,"mid",mid,"high",high)

    elif a[mid]<key:
        low = mid+1
    else:
        high = mid-1
print(a[foundAt], " at location",foundAt)
print(countOfKey)

""""
            while foundAt>=0 and a[foundAt]==key:
                countOfKey += 1
                foundAt -= 1
            while foundAt+1<high and a[foundAt]==key:
                 countOfKey += 1
                 foundAt += 1
"""
