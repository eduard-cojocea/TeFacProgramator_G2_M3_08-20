import json

with open("countries.json", "r") as f:
    data = json.load(f)
    
print(data)
print(type(data))

print(json.dumps(data))
print(json.loads(json.dumps(data)))

print(json.dumps(data, indent=4))