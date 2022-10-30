"""
Heroku Api test script
"""
import requests


data = {
    "age": 30,
    "workclass": "Private",
    "education": "Some-college",
    "maritalStatus": "Separated",
    "occupation": "Transport-moving",
    "relationship": "Husband",
    "race": "Black",
    "sex": "Male",
    "hoursPerWeek": 40,
    "nativeCountry": "United-States"
    }
r = requests.post('https://ml-heroku-fastapi.herokuapp.com/', json=data)

assert r.status_code == 200 # 200 indicates that the request has succeeded

print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())