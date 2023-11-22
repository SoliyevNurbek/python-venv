import requests
import json


def get_user():
    response = requests.get('https://randomuser.me/api/')
    
    if response.status_code == 200:
        content = response.content
    
        data = json.loads(content.decode())
    
        randomuser = data['results'][0]
    
        user = {
            "fullname": f"{randomuser['name']['first']} {randomuser['name']['last']}",
            "email": randomuser['email'],
            "phone": randomuser['phone'],
            "age": randomuser['dob']['age'],
        }
    return user

def get_n_users(n: int) -> list[dict]:
    users = []
    for i in range(n):
        user = get_user()
        users.append(user)

    return {"users": users, "info": {"count": n}}

def write_users(users: dict):
    with open('users.json', 'w') as f:
        data_json = json.dumps(users, indent=4)
        f.write(data_json)

users = get_n_users(31) 
write_users(users)
