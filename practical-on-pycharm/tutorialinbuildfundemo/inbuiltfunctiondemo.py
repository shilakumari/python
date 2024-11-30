"""print(pow(2, 3)) #8
print(round(-31.1221, 2)) #-31.12
print(round(-31.156, 2)) #-31.16
print(round(-31.154, 2)) #-31.15
print(round(-31.187, 2)) #-31.19
print(round(-31.185, 2)) #-31.18
print(round(-31.186, 2)) #-31.19

text="hello"
print(text.upper()) #HELLO
print(len(text)) #5
print(text.replace("l","e",1))

sentence = " Hello World!"
print(sentence.strip())
print(sentence.split(" "))
print("-".join(sentence.split()))

txt ="Hello-good-morning-World-Python"
part = txt.split("-",3) #Hello World-Python
result = ",".join(part[::-1]) #World-Python,morning,good,Hello
print(result)"""

x="10"
if isinstance(x, int) or type(x) == int:
    print("It's an integer")
else:
    print("It's not an integer")