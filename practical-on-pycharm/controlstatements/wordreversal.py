s="All the power is with in you"
lst=s.split(' ')
print(lst)

i=len(lst)-1
rev=[]
while i>=0:
    rev.append(lst[i])
    i=i-1
print(rev)
output=" ".join(rev)
print(output)