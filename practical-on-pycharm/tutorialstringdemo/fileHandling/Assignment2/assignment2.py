name=input()
age=input()

with open("info.txt","w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}")
print("Data saved successfully!")

with open("info.txt","r") as f:
    d=f.read()
    print(d)