
def firstNonRepeatingChar(s):

    for i in range(len(s)):
        isFound = False
        for j in range(len(s)):
            if(i !=j and s[j]== s[i] ):
                isFound = True
                break
        if isFound == False :
            return s[i]
    return "-1"



s="aabc"
s="gjejfjpomhibmmfknofoijkkfniajbomlcfgmldednmcghopekhjppbk"
#s="ibwoasdelskfocvslhgdifubspagnclwzclaixyalhbmlglvot"
#s="aabc"  #a-1bb
for i in range (len(s)):
    print(firstNonRepeatingChar(s[0:i+1]),end=' ')

