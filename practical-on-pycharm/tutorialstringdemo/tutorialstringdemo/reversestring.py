def reverseString(s):

    revStr = ""

    for i in range(len(s)-1,-1,-1):
        revStr += s[i]

    return revStr

print(reverseString("Hello"))
