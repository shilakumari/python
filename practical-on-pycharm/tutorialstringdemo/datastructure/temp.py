x=9
name = "rahul" if x>10 else  "praveen" if x<8 else "siya"
print(name)

#Above code can be written as below
if x>10:
    print("rahul")
else:
    if x<8:
        print("praveen")
    else:
        print("siya")

x=10
print(isinstance(x, int))
if type(x)==int:
    print("True")

def drawWShape(size):
    for i in range(size):
        print(" "*i+"\\"+" "*(2*(size-i-1))+"/", end="")
        print(" "*(2*i)+"\\", end="")
        print(" "*(2*(size-i-1))+"/")
drawWShape(5)

s="12345678"
print(s.isdigit())#True

wrd=["hi","hello","namaste"]
print(" ".join(wrd))

l=[1,2,3,4,5]
print(sum(l))

dict1 = {"a":1,"b":2}
print(dict1)#{'a': 1, 'b': 2}

my_list = [1, 2, 3, 4]
my_list[1] = 10
print(my_list)


#print C
size=5
for i in range(size):
    if i==0 or i==size-1:
        print("* "*size)
    else:
        print("*")
print()

#print U
size=5
for i in range(size):
    if i==size-1:
        print("* "*size)
    else:
        print("* "+" "*size +" *")

N=5
for i in range(N, 0, -1):
    for j in range(1, i+1):
        print("*",end='')
        if j!=i:
            print(" ",end='')
    for j in range(i, N):
        print(" "*2, end='')
    print()

string="Samantha a hidden message."
vowels="AaEeIiOoUu"
c = [c for c in string if c not in vowels]
print(c)
consonants = "".join(letter for letter in c if letter.isalpha())
print(consonants)
consonantsCount = len(consonants)
print(consonantsCount)