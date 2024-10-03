# list of country with 3 data
# add country at the end
# remove by index
#add a country in the middle

lst=["India","USA","Australia"]
print(lst)

lst.append("China")
print(lst)

del lst[3]
print(lst)

lst.insert(2,"France")
print(lst)

# Using Set
s={"India","USA","Australia"}
print(s)

s.add("China")
#s.update(["China"])
print(s)

#Indexing not allowed in set, remove by index not possible
#del s[3]

#Insertion order not preserved, insert at middle not possible
print(s)