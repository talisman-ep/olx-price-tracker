import json
import os

def save_price(price):
    data = {
        "price": price
    }
    
    with open("price.json", "w") as last_price:
        json.dump(data, last_price, indent=4)

def load_price():
    if not os.path.exists("price.json"):
        return None
    
    try:
        with open("price.json", "r") as last_price:
            data = json.load(last_price)
            return data.get("price")
    except Exception as e:
        print(f"Error loading price: {e}")
        return None