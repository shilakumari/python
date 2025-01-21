s="Python is cool"
temp = s.split(" ")
print(temp)

#Using reversed()
i=0
'''while i<=len(temp)-1: 
    s1=temp[i]
    print(''.join(reversed(s1)),end=' ')
    i=i+1'''

r=[]
while i<len(temp):
    r.append(temp[i][::-1])
    i=i+1
print(r)
outputs=' '.join(r)
print(outputs)

