import requests 
res =requests.post("https://locationappp.herokuapp.com/add",data = {
    "latitude":11.0768,
    "longitude":77.1419,
    "total_people":5,
    "violated_people":4

    }).json()
print(res)