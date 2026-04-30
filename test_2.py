#this expands on test_1 and formats the price data in classes so data can be tabulated nicely when printed.

from tabulate import tabulate
import requests
from config import CSFLOAT_API_KEY


headers = {
    "Authorization": CSFLOAT_API_KEY
}


def format_data(name,float_category,float,price,rarity):
    formatted = [name,float_category,round(float,4),f'£{price/100}',rarity]
    return formatted

class Skin():
    def __init__(self,float,price,name,rarity,float_category):
        self.float = float
        self.price = price
        self.name = name 
        self.rarity = rarity
        self.float_category = float_category
    def __repr__(self):


def define_float_category(float_value):
    if float_value < 0.07:
        return "Factory New"
    elif float_value < 0.15:
        return "Minimal Wear"
    elif float_value < 0.38:
        return "Field-Tested"
    elif float_value < 0.45:
        return "Well-Worn"
    else:
        return "Battle-Scarred"

def get_ak_deals(price_limit_low, price_limit_high, float_limit_low, float_limit_high, deals_shown, sort_by="best_deal"):
    params = {
    "limit": deals_shown,
    "sort_by": sort_by,
    "type": "buy_now",
    "max_float": float_limit_high,
    "min_float": float_limit_low,
    "min_price": price_limit_low,
    "max_price": price_limit_high,
    "category": 0,
    "def_index": 7
}

    try:
        response = requests.get(
            "https://csfloat.com/api/v1/listings",
            headers=headers,
            params=params,
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch listings: {e}")
        return

    data = response.json()
    if "data" not in data:
        print("Unexpected API response format: missing 'data' field.")
        return

    listings = data["data"]
    
    seen = set()
    for listing in listings:
        item = listing["item"]
        name = item["item_name"]
        
        if name in seen:
            continue  # skip duplicates 
        
        seen.add(name) 

        print(
            f"Item: {name} | "
            f"Price: £{listing['price']/100} | "
            f"Float: {round(item['float_value'],4)} "
            f"({define_float_category(item['float_value'])})"
        )
get_ak_deals(price_limit_low=1000, 
             price_limit_high=100000, 
             float_limit_low=0.0, 
             float_limit_high=1.0, 
             deals_shown=10)