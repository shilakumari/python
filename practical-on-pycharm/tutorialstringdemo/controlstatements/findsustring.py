s="Take up one idea and make idea in your life"
subs="idea"
pos=-1
found=False
length=len(s)

while True:
    pos=s.find(subs,pos+1,length)
    if pos == -1:
        break
    print("found the substring at position",pos)
    found=True
if found==False:
    print("substring not found")
