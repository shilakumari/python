import  re

str = "Take up one-idea in 1-2-2020, one-idea at a time only in 2-4-2025"

# with '^' regex should occur right at the beginning of string
#If not matched then return none
result = re.search(r'^o\w',str)
print(result)#None

result = re.search(r'^T\w',str)
print(result.group())#Ta
result = re.search(r'^T\w*',str)
print(result.group())
