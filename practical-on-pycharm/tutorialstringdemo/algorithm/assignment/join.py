#arg1:list of string, agr2:seperator
def join(l, seperator):
    temp=''
    length = len(l)
    for i in range(length):
        temp += l[i]
        if i != length-1:
            temp += seperator
    return temp


l1 = ['Hello', 'World']
s = join(l1,' ')
print(s)