x=1
with open("data.txt","r") as f:
    data=f.readlines()
    for i in range(len(data)):
        print(f"Line {i+1}:",data[i].strip())