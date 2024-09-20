import requests

request = requests.get('http://127.0.0.1:8000/random/56')
print (request.json())


