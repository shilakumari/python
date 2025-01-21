#s = "hi there"
#s = "hello world"
s = "a b"
l = list(s)
rs = ""
print(l)
i=0

while i<len(l):
    count = 0
    if l[i]==" ":
        rs += l[i]
        i += 1
    else:
        while i<len(l) and l[i]!=" ":
            count += 1
            i += 1
    for k in range(count):
        rs += l[i-1-k]

print(rs)
