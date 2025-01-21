s1="You are awesome"
s2="""You are 
the creator 
of your own destiny"""
print(s2)

#Indexing
print(s1[3])

#reputation
print(s1*2)

print(len(s1))
print(len(s2))


#Slicing
print(s1[0:5])#doesnot include 5
print(s1[0:])
print(s1[:8])#include 0 to 7
print(s1[-3:-1])# - mean index from last

#Slicing using third value
print(s1[0:9:2])#Yuaea
print(s1[15::-1])#emosewa era uoY
print(s1[::-1])#emosewa era uoY

s3=" You are awesome "
#Remove spaces
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())

print(s3.find("awe", 0, len(s3)))
print(s3.count("a"))
print(s3.replace("awesome","super"))

print(s3.lower())
print(s3.upper())
print(s3.title())