with open("student.txt","w") as f:
    f.write("Shila\nRam\nShyam")

with open("student.txt","r") as f:
    for line in f:
        print("Student:",line.strip())
#o/p:
#Student: Shila
#Student: Ram
#Student: Shyam

#Serialization
d={"id":1, "courses":["Math","Art"]}
import pickle
with open("pickle-file.pkl","wb") as f:
    pickle.dump(d,f)
#Deserializing
with open("pickle-file.pkl","rb") as f:
    pobj = pickle.load(f)
    print(pobj["courses"])


