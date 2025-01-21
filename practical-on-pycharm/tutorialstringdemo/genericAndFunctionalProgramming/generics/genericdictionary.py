from typing import Dict
myDict: Dict[str, int]={"a":1, "bc":2}
print(myDict["bc"])#2
d={}
l=[1,2]
for key,value in myDict.items():
    if myDict[key]==l[1]:
        d[key]=value
print(d)
