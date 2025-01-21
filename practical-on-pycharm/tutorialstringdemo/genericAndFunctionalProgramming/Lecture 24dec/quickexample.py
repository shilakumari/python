data=["5","12","Hello","3","world"]
result=list(map(lambda x:int(x)*2 if x.isdigit() else len(x), data))
print(result)#[10, 24, 5, 6, 5]

data2=[10,15,20,25]
result=list(filter(lambda x:x%2==0, map(lambda x:x-5, data2)))
print(result)#[10, 20]

words=["apple","","banana","","cherry"]
filtered = list(filter(lambda x:x.strip()!="", words))
print(filtered)

nums=[-10, 0, 5, 8, -3, 15]
result=list(filter(lambda x:x%2==0,map(abs,nums)))
print(result)#[10, 0, 8]

data=[(1,2),(3,4),(5,6)]
result=list(map(lambda x: x[0]+x[1],data))
print(result)#[3, 7, 11]

str1=["hello", "world","python"]
result=list(map(lambda s:s[::-1].upper(), filter(lambda x: len(x)>5, str1)))
print(result)#['NOHTYP']

