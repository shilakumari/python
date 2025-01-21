vowels=['a','e','i','o','u']
l='c'
flag = False
for i in range(len(vowels)):
    if l in vowels[i]:
        flag=True
if flag:
    print(f" {l} is vowel")
else:
    print(f" {l} is consonant")

