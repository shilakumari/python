inputList = [1,1,1,2,1,2,2,3,1]
myCountDict={}
for v in inputList:
    if v not in myCountDict.keys():
        myCountDict[v] = 1
    else:
        myCountDict[v] += 1

print(myCountDict)