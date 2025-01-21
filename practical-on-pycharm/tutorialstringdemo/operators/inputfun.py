"""s=input()
print(s)

#By default input() give string type
s=input("Enter your name:")
print(s)
i=int(input("Enter a integer number:"))
print(i)
print(type(i))"""

#Reading multiple inputs
#By default split() uses space as a seperator
lst=[x for x in input("Enter three numbers separated by space").split()]
print(lst)
#by default input is string
lst=[x for x in input("Enter three numbers separated by comma").split(',')]
print(lst)
#input typecast in integer
lst=[int(x) for x in input("Enter three numbers separated by comma").split(',')]
print(lst)
#input typecast in float
lst=[float(x) for x in input("Enter three numbers separated by comma").split(',')]
print(lst)