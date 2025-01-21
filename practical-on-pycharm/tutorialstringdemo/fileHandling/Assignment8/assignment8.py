import pickle
scores = [88, 92, 79, 93, 85]

with open("scores.pkl","wb") as f:
    pickle.dump(scores,f)

with open("scores.pkl","rb") as f:
    data = pickle.load(f)
    print(data)
#o/p: [88, 92, 79, 93, 85]