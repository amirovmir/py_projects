import requests

r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, r.text, r.json())

new_user = [{
    "id": "3",
    "name": "Peter",
    "surname": "Green"
}]

r = requests.post('http://127.0.0.1:5000/users', json={"name": "Peter", "surname": "Green"})
print(r.json())

r = requests.put('http://127.0.0.1:5000/users/1', json={"id": "1", "name": "Mark"})
print(r.json())
