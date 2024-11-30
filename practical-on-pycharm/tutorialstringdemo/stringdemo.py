s = "hi python !"
print(type(s))
print("hi" in s)#True

# ''' for multiple lines
s1 = '''hi python !
    having fun.
'''
print(s1)

#string concatenation
space=' '
print("Shila"+space+"Kumari")
#String repeat
print("-"*10)

#Indexing
s2 = "Python"
print(s2[0])
print(s2[0]," ", s2[-1])

#Slicing
print(s2[1], s2[-2], s2[3:6])
print(s2[-1:0:-1])
print(s2[-1::-1])
print(s2[::-1])
print(s2[::1])

txt = "They said, \t \"how are you?\""
print(txt)
txt = "They said, \n \"how are you?\""
print(txt)
txt = "They said, \v \"how are you?\""
print(txt)

#Skipping character while slicing
#It is possible to skip characters while slicing by passing step arguments
language = "Python"
pto = language[0:6:2]
print(pto)#Pto


