#Created notes.txt with content "Hello World\n"
"""with open("notes.txt","w") as f:
    f.write("Hello World\n")
"""

#notes.txt with empty content
"""with open("notes.txt","w") as f:
    pass
"""

#notes.txt with content Hello World\ni got it
with open("notes.txt","w") as f:
    f.write("Hello World\ni got it\n")

#"a" append mode
with open("notes.txt","a") as f:
    f.write("Thank you everyone")
