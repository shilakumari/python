def counts(itr,k):
    c=0
    for i in range(len(itr)):
        if k==itr[i]:
            c += 1
    return c

print(counts([1,2,2,3,4,2],2))
print(counts('Hello world','o'))
