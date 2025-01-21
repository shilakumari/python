import json
with open("data.json","r") as f:
	info=json.load(f)
	print(info["name"])#o/p: Bob

