import requests

servise = ("http://127.0.0.1:5000/users")
req = requests.get(servise)
j_api = req.json()
links = [item["link"] for item in j_api]
print(links)