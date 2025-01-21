import json
data={"name":"Bob", "age":25}
with open("data.json","w") as f:
	json.dump(data,f)
