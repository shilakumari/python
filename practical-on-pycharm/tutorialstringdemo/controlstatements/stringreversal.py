s=input("Enter a string")

#print(s[::-1])

'''result=''
i=len(s)-1
while i>=0:
    result=result+s[i]
    i=i-1
print(result)'''

#Reverse using join()
print( ''.join(reversed(s)))