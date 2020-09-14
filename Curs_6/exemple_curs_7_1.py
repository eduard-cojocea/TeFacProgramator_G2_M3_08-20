import json

my_dict = {
    "SPQR": "Roma",
    "Dacia": "Sarmizegetusa",
    "Cartagina": "Cartagina"
}

with open("countries.json", "w") as f:
    json.dump(my_dict, f, indent=4)