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

# Test post request json
params = {'name': "Harry Potter", 'value': 5.00}
response = requests.post('http://localhost:8000/other', json = params)
data = response.json() # if response in json
print(data)

# Test post db
params = {'filename': "Magazines.zip",'title': "Javax",'content': "18sx"}
response = requests.post('http://localhost:8000/notes', json = params)
data = response.json() # if response in json
print(data)

# Test get db
title= "Learning Python Db"
response = requests.get(f'http://localhost:8000/notes/str/{title}')
data = response.json() # if response in json
print(data)

# Test get db json
params = {'title': 'Learning Python Db'}
response = requests.get(f'http://localhost:8000/notes/json', json = params)
data = response.json() # if response in json
print(data)

# Test get db manual query
params = {'title': 'Learning Python Db'}
response = requests.get(f'http://localhost:8000/notes/query', json = params)
data = response.json() # if response in json
print(data)
