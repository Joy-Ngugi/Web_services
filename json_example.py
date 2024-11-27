import json

teachers = """
[
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Joy", "email": "joy@example.com"},
    {"id": 4, "name": "Peter", "email": "peter@example.com"},
    {"id": 5, "name": "James", "email": "james@example.com"}
]
"""
#converts the json into a dict
users = json.loads(teachers)     
for user in users:
    print(f"Name: {user['name']}, Email: {user['email']}")
    
    
#converting a dict to a json string
teachers = [
    {"id": 1, "name": "Peter", "email": "peter@example.com"},
    {"id": 2, "name": "James", "email": "james@example.com"}
]

users_json=json.dumps(teachers)
users = json.loads(users_json)
for user in users:
    print(f"Name: {user['name']}, Email: {user['email']}")
    

#converting a dict to a json string using pretty-printing for more legibility  
users_json=json.dumps(teachers, indent=4)


#writing JSON to a file
data = {
    "name":"Angie",
    "age":43
}
with open('data.json', 'w') as file:
    json.dump(data, file)


#reading JSON to a file
with open('data.json', 'r') as file:
    data = json.load(file)
    
    print(data["name"])
    print(data["age"])