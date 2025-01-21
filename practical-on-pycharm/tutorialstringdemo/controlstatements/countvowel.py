#Count vowel
word=input("Enter a word")
vowels={'a','e','i','o','u'}
i=0
for c in word:
    if c in vowels:
        i+=1
print("Count of vowel ",i)

#Count and return vowel
#taking dictionary
result={}
for c in word:
    if c in vowels:
        result[c]=result.get(c,0)+1

for k,v in result.items():
    print(k,"is of",v,"times")
