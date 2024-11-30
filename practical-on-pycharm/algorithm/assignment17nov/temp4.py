
days=["SSSSEEEECCCCEECCCC","CCCCCCCCCCCCC","CCCCCSSSSEEECCCCSS","CCCCCCCCCCCC","SSSSSEEESSCCCCCCCS",
    "EESSSSCCCCCCSSEEEE"]
n= len(days)
dayMaxCount=0
totalMaxCount=0
endFlag = False
endCount=0
startFlag =False
dayCount=0
for i in range(n):
    count=0
    dayCount=0
    day = days[i]
    n2=len(day)
    #print(s1)
    for j in range(n2):
        if day[j]=="C":
            if j == 0 :
                startFlag = True
            count += 1
            if j == n2-1:
                endFlag = True
                endCount =count
        else:
            if count > dayCount:
                dayCount=count
            #print(i, count,dayCount, endFlag, endCount, startFlag)
            if endFlag == True and startFlag == True:
                if dayCount == 13:
                    if endFlag == True:
                        endCount += dayCount
                if totalMaxCount < count+endCount:
                    totalMaxCount =  endCount +count
                    #print(totalMaxCount)
            count = 0
            startFlag= False
            endFlag = False
            endCount = 0
        if j == n2-1:
            if count > dayCount:
                dayCount=count
    if dayMaxCount<=dayCount:
        dayMaxCount=dayCount
        if totalMaxCount < dayMaxCount :
            totalMaxCount = dayMaxCount
    print(i, count, dayCount, dayMaxCount)
    #print(i,dayCount, endFlag, endCount, startFlag)

print("dayMaxCount",dayMaxCount)
print("totalMaxCount",totalMaxCount)



