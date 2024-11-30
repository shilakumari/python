def find(s,substr):
    pos=-1
    temp=""
    flag=False
    for i in range(0,len(s)):
        i1=i
        if s[i1]==substr[0]:
            for j in range(len(substr)):
                if s[i1+j] ==substr[j]:
                    if j == len(substr)-1:
                        flag = True
                        pos=i1
                else:
                    break
        i1=i
    return pos

s="Look for the substring in this string"
print(find(s,"substring"))

