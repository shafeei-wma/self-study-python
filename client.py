# run client req by type this in terminal --> python client.py
import requests

# DB_PORT = '8080' # Enable this if test for docker localhost
DB_PORT = '8000' # Enable this if test for traditional localhost

# Test normal get
response = requests.get(f'http://localhost:{DB_PORT}')
print('1:: ',response.text)

# Test post
params = {'myKey': 300}
response = requests.post(f'http://localhost:{DB_PORT}/new', json = params)
data = response.json() # if response in json
print('2:: ',data)
print('2:: ',data["res"])

# Test post request json
params = {'name': "Harry Potter", 'value': 5.00}
response = requests.post(f'http://localhost:{DB_PORT}/other', json = params)
data = response.json() # if response in json
print('3:: ',data)

# Test post db
params = {'filename': "Magazines.zip",'title': "Learning Python Db",'content': "18sx"}
response = requests.post(f'http://localhost:{DB_PORT}/notes', json = params)
data = response.json() # if response in json
print('4:: ',data)

# Test get db
title= "Learning Python Db"
response = requests.get(f'http://localhost:{DB_PORT}/notes/str/{title}')
data = response.json() # if response in json
print('5:: ',data)

# Test get db json
params = {'title': 'Learning Python Db'}
response = requests.get(f'http://localhost:{DB_PORT}/notes/json', json = params)
data = response.json() # if response in json
print('6:: ',data)

# Test get db manual query
params = {'title': 'Learning Python Db'}
response = requests.get(f'http://localhost:{DB_PORT}/notes/query', json = params)
data = response.json() # if response in json
print('7:: ',data)
