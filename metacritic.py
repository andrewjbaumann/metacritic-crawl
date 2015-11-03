import json

def add(x,y): return x+y

with open('kimonoData.json') as data_file:
	data = json.load(data_file)
	
# print(data["results"]["collection1"][0]["acc_score"])

acc_list = []

for x in data["results"]["collection1"]:
	acc_list.append(int(x["acc_score"]))
	
avg_critic = reduce(add, acc_list)
avg_critic = total / len(acc_list)

print total