colors ={"red", "green","blue"}
colors.add("yellow")
print(colors) #{'yellow', 'green', 'blue', 'red'}

set1 = {1,2,3,4}
set2 = {3,4,5,6}
result = set1&set2 | set1-set2
#set1&set2 = {3,4}
#set1-set2 = {1,2}
print(result) #{1, 2, 3, 4}

#to add items, update()
f1 = {"apple","banana","cherry",}
tropical = {"pineapple", "mango","papaya"}
f1.update(tropical)
print(f1)#{'banana', 'mango', 'papaya', 'apple', 'cherry', 'pineapple'}
print(tropical)#{'mango', 'papaya', 'pineapple'}

#To remove items, remove()
f1.remove("papaya")
print(f1)#{'pineapple', 'apple', 'cherry', 'banana', 'mango'}
x=f1.pop()
print(f1)#{'apple', 'cherry', 'banana', 'mango'}

#union() or "|" to add set
s1={"a","b","c"}
s2={1,2,3}
s3 = s1.union(s2)
print(s3)#{'c', 1, 'a', 2, 3, 'b'}

s4 = s1|s2
print(s4)#{1, 2, 3, 'c', 'b', 'a'}