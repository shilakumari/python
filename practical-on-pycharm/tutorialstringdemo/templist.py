myList=[["banana","cherry"],["mango","apple"]]
print(myList[1][1])
print(myList[-1][-1])
print(myList[0:1])
myList2=["Apple","Banana","Cherry","Kiwi","Mango"]
print(myList2[0:3])
print(myList2[:3])
print(myList2[-4:-1]) # -4 is Banana to before -1

myList2.insert(2,"Watermelon")
print(myList2)

myList2.append("orange")
print(myList2)

#To append elements from another list to the current list, use extend() method
l=["apple","banana","cherry"]
l2=["mango","pineapple"]
l.extend(l2)
print(l)


# remove() remove the first first instance of the same value
list1=["aaa","bbb","aaa","ccc","ddd"]
list1.remove("aaa")
print(list1) #["bbb","aaa","ccc","ddd"]

#pop() removes the specified index
list1.pop(0)
print(list1)
list1.pop()#removes from last
print(list1)

