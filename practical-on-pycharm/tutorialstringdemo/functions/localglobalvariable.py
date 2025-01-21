#Global variable
x=123
def display():
    # Local variable
    x=678
    print(x)
    # Accessing global variable
    print(globals()['x'])

print(x)
display()

#Assign function to a variable
y=display
y()
y()

