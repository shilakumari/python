import re
str ="Take up one idea, one idea at a time"
result1 = re.search(r'o\w',str)
result2 = re.search(r'o\w\w',str)
print(result1.group())
print(result2.group())

#findall() find the all matching word and store it into list
result3 = re.findall(r'o\w\w',str)
print(result3)

#match() method only search at the beginning of the string
result3 = re.match(r'o\w\w',str)
print(result3)#None, because at the beginning is 'Take'

result3 = re.match(r'T\w\w',str)
print(result3.group())#Tak

#substitute method regex
result4 = re.sub(r'one','two',str)
print(result4)

str1 ="Take 1 up one 23 idea, one idea 45 at a time"
# split() method split the string based on regex
result5 = re.split(r'\d',str1)
print(result5)
