# utils/template_utils.py

import os
import json

TEMPLATE_FILE = "templates/saved.json"

def ensure_file():
    if not os.path.exists("templates"):
        os.makedirs("templates")
    if not os.path.exists(TEMPLATE_FILE):
        with open(TEMPLATE_FILE, "w") as f:
            json.dump({}, f)

def load_all():
    ensure_file()
    with open(TEMPLATE_FILE, "r") as f:
        return json.load(f)

def save_all(data):
    with open(TEMPLATE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def save_template(user_id, name, template_data):
    data = load_all()
    if user_id not in data:
        data[user_id] = {}
    data[user_id][name] = template_data
    save_all(data)

def load_template(user_id, name):
    data = load_all()
    return data.get(user_id, {}).get(name)

def list_templates(user_id):
    data = load_all()
    return list(data.get(user_id, {}).keys())

def delete_template(user_id, name):
    data = load_all()
    if user_id in data and name in data[user_id]:
        del data[user_id][name]
        save_all(data)
        return True
    return False
