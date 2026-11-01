import json

INVENTORY_FILE = "inventory.json"  

def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory(data):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(data, file, indent=4)