import requests
import json

data = {    "age": 30,
    "workclass": "Private",
    "education": "Some-college",
    "maritalStatus": "Separated",
    "occupation": "Transport-moving",
    "relationship": "Husband",
    "race": "Black",
    "sex": "Male",
    "hoursPerWeek": 40,
    "nativeCountry": "United-States"}

r = requests.post("http://127.0.0.1:8000", data=json.dumps(data))

print(r.json())