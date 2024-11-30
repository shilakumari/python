#s="aabc"
s="gjejfjpomhibmmfknofoijkkfniajbomlcfgmldednmcghopekhjppbk"
s1=""
i=0
while i<len(s):
    ts=s[i]
    #print("i",i)
    #print(ts)
    s1 += ts
    j=i+1
    while j<len(s):
        #print("j",j)
        if s[j]==ts:
            s1 += " "+"-1"
            j += 1
            break
        else:
            s1 += " "+ts
        j += 1

    i += j

print(s1)