import pickle
data={
		"name":"Shila Kumari",
		"age":27
}
#Serializing data to a pickle file
with open("data.pkl","wb") as pickle_file:
	pickle.dump(data, pickle_file)
#Deserialize data to a pickle file
with open("data.pkl","rb") as file:
	data = pickle.load(file)
	print(data)