import json

with open('personnage.json') as f:
  source = f.read()

data = json.loads(source)

with open('personnage.json', 'w') as f:
  json.dump(data, f, indent=2)

#data2=json.load(data)
#data3=data2["0"]
#print(data3["cheveux"])

for i in data['possibilites']:
    for k in i:
        print(k)
