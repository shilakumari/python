print(True and False or True)
print(bool(''))
one =2
two=4
def evenodd():
    if (one % 2 == 0) and (two % 2 == 0):
        print("Even")
    elif (one % 2 != 0) and (two % 2 != 0):
        print("Odd")
    else:
        print("Even-Odd")

evenodd()