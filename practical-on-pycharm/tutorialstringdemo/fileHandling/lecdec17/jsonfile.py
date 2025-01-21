import json
data = {
    "name": "Shila Kumari",
    "age":27
}

# Serializing data to a json file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Deserialize the data from the json file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
