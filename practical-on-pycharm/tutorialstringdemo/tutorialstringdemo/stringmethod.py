s="Hello"
#To reverse 's'
print(s[-1::-1])

print(type(s))

s.replace("H","B")
print(s)

text="Python is fun!"
print(text[:6]+text[-4:-100:-1])

text="Python"
print(text[::-1]==text[-1::-1])


#String Formatting Methods
name="alice"
age=25.50

#old style using %
print("name is %s and age is %8f" %(name,age))
print("name is %s and age is %10f" %(name,age))
print("name is %s and age is %.2f" %(name,age))
print("name is %s and age is %.1f" %(name,age))
print("name is %s and age is %.0f" %(name,age))
#print("name is %s and age is %.-1f" %(name,age))#Not allowed

# .format() method
print("name is {} and age is {}".format(name, age))

# using f-String (Python 3.6+)
print(f"name is {name} and age is {age}")

s4 = '\t Hi \n'
print(s4.strip())
sent = "\t  My Python class is on "
print(sent.split())
print(sent.strip().split())

txt = "Python is fun and Python is powerful!"
print(txt.replace("Python", "Java", 1))# here 1 means one instance
print(txt.count("is"))

#count() returns occurrence substring in string,count(substring,start=..,end=..)
challenge = "thirty days of Python"
print(challenge.count("y"))

#endswith() checks if a string ends with a specified ending
print(challenge.endswith("on"))

#find() returns index of first occurrence of a substring, if not return -1
challenge = "thirty days of Python"
print(challenge.find("y"))#5
print(challenge.find("th"))#0

#rfind() returns index of last occurrence of a substring, if not return -1
print(challenge.rfind("y"))#16
print(challenge.rfind("th"))#17

#format() formats string into a nicer output
name="hi Mandi"
age=250
job="teacher"
sentence = "I am {}. I am a {}. I am {} years old".format(name,job,age)
print(sentence)

#index() return the lowest index of a substring, we can specify the start index index(substr,startIndex)
challenge = "thirty days of Python"
subStr = "th"
print(challenge.index(subStr))
print(challenge.index(subStr,9))

#rindex() return the highest index of a substring
challenge = "thirty days of Python"
subStr = "th"
print(challenge.rindex(subStr))

#isalnum() checks alphanumeric character
alphaNum = "ThirtyDaysOfPython1234"
print(alphaNum.isalnum())#True
print("ThirtyDaysOfPython 1234".isalnum())#Flase, because of space

#iddecimal() check if all characters in a string are decimal(0-9)
deci = "123"
print(deci.isdecimal())#True
deci = "\u00B2"
print(deci.isdecimal())#False
deci = "12 3"
print(deci.isdecimal())#Flase

#isdigit() check if all characters in a string are numbers
dig = "Thirty"
print(dig.isdigit())
dig = "30"
print(dig.isdigit())
dig = "\u00B2"
print(dig.isdigit())
