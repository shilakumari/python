import os
print(os.path.exists("notes1.txt"))#False
if os.path.exists("notes1.txt"):
    os.remove("notes1.txt")

print(os.path.exists(r"notes1.txt"))#False, here r means relative path
if os.path.exists(r"notes1.txt"):
    os.remove("notes1.txt")

