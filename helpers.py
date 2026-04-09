import json

def load_users():
    with open('./users.json',"r") as f:
        users = json.load(f)
        return users
    
def save_users(data):
    with open('./users.json', "w") as f:
        json.dump(data, f)

def normalize_phone(number: str):
    if "+91-" in number:
        return number.replace("+91-", "").replace(" ", "")
    return number.replace(" ", "")