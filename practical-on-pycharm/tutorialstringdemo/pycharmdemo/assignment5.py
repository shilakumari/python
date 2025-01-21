#Dictionary
#student_info- name, age and major
student_info={"name":"XYZ","age":22,"major":"Physics"}

#Print name and age
print("Student Name:",student_info["name"],"Age:",student_info["age"])

#Add new key email
student_info.update({"email":"sijla1234kuma@gmail.com"})

#Update the age
student_info.update({"age":"23"})

key=student_info.keys()
for eachkey in key:
    print(student_info[eachkey])

#Remove the key major
del student_info["major"]

print("After deleting major key")
for eachkey in key:
    print(student_info[eachkey])
