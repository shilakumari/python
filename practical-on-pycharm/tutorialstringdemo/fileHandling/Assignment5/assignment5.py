import json

person = {
    "name": "John",
    "age": 28,
    "skills": ["Python", "Django", "Machine Learning"]
}

with open("person.json","w") as f:
    json.dump(person,f)

with open("person.json","r") as f:
    data=json.load(f)
    for skill in data["skills"]:
        print(skill)