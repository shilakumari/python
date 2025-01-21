#equ="{(([])}"
#equ="([]"
#equ="())))))"
#Using List
"""l=[]
open_br=["{","[","("]
close_br=["}","]",")"]
cl=[]
for br in equ:
    if br in open_br:
        l.append(br)
    elif br in close_br:
        if len(l)==0:
            #print("not balanced")
            cl.append(br)
            break
        v=l.pop()
        if open_br.index(v)==close_br.index(br):
            continue
        else:
            #print("not balanced")
            break

#print(l)
if len(l)==0 and len(cl)==0:
    print("balanced")
else:
    print("not balanced")"""

#Using dictionary
equ="{([])}"
mydict={"(":")","[":"]","{":"}"}
open_br=""
flag=True
for letter in equ:
    if letter in mydict.keys():#open bracket
        open_br=letter
    elif letter in mydict.values():
        if mydict[open_br]==letter:
            print("balanced")
            continue
        else:
            flag=False
            print("not balanced")
            break
