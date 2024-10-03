s="aaaaaBbbbbbcCCdd"
results=[]

for c in s:
    if c not in results:
        results.append(c)

outputs=''.join(results)
print(outputs)
