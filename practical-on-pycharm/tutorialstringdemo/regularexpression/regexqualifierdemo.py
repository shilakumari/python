import  re

str ="Take up one-idea in 1-2-2020, one-idea at a time only in 2-4-2025"

#w+ means 1 or more repetitions
result = re.findall(r'o\w+',str)
print(result)

#W* means 'o' followed by 0 or more repetitions
result = re.findall(r'o\w*',str)
print(result)

#w? means 0 or 1
result = re.findall(r'o\w{1,2}',str)
print(result)

#{m} means m number of occurence
result = re.findall(r'o\w{3}',str)
print(result)
#{m,n} means minimum 'm' and maximum 'n' number of occurence
result = re.findall(r'o\w{1,2}',str)
print(result)

#matching date
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)

