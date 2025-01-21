a1=[1,2,2,3,4,5,1]
a2=[4,4,3,2,1,1]
count=0
for i in a1:
    if i in a2:
        a2.remove(i)
        count +=1
print(count)

#Correct but inefficient way