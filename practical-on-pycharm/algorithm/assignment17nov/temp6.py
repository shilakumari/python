def binarySearch(a,key,firstOrLast):
    foundAt=-1
    low=0
    high=len(a)-1
    l=[]
    while low<=high:
        mid=(low+high)//2
        if a[mid]==key:
            foundAt = mid
            if firstOrLast == 'FIRST' :
                high = mid-1
            if firstOrLast == 'LAST':
                low=mid+1
        elif a[mid]<key:
            low = mid+1
        else:
            high = mid-1
    return foundAt

a=[1,1,1,1,2,2,2,2,2,3]
key=3
#o/p: 0 3 4
firstOccurs=binarySearch(a,key,"FIRST")
lastOccurs=binarySearch(a,key,"LAST")
countOfKey=lastOccurs - firstOccurs+1
print(firstOccurs,lastOccurs,countOfKey)
