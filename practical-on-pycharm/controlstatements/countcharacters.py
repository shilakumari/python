s="aaaaaBbbcCdd"
temp={}

for c in s:
    if c in temp.keys():
        temp[c]=temp[c]+1
    else:
        temp[c]=1

for k,v in temp.items():
    #print(k,"=",v,"times")
    print("{}={} times".format(k,v))