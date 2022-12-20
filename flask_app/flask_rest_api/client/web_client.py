import requests

r = requests.post('http://127.0.0.1:5000/users', json={"name": "Michael", "surname": "Johnson", "tel": "16513584159"})

r = requests.get('http://127.0.0.1:5000/users')

#r = requests.get('http://127.0.0.1:5000/users/2')

r = requests.delete('http://127.0.0.1:5000/users/1')

r = requests.get('http://127.0.0.1:5000/users')

r = requests.put('http://127.0.0.1:5000/users/2', json={"name": "Mike", "surname": "Groot", "tel": "16513584159"})

r = requests.get('http://127.0.0.1:5000/users')
