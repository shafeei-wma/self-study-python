# run client req by type this in terminal --> python client.py
import requests

# Test normal get
response = requests.get('http://localhost:8000')
print(response.text)

# Test post
params = {'myKey': 300}
response = requests.post('http://localhost:8000/new', json = params)
data = response.json() # if response in json
print(data)
print(data["res"])
