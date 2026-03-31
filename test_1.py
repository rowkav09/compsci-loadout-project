#test 1 is to make a program in the cli that gets the best ak deal/ discount/ price etc.. for a ceartain price range and float range

import requests
from config import CSFLOAT_API_KEY

headers = {
    "Authorization": CSFLOAT_API_KEY
}

params = {
    "limit": 5,
    "sort_by": "best_deal",
    "type": "auction",
    "max_float": 0.1,
    "min_float": 0.0,
    "min_price": 1000,
    "max_price": 100000,
    "category": 0,
    "def_index": 7
}

response = requests.get("https://csfloat.com/api/v1/listings", 
                        headers=headers,
                        params=params)
data = response.json()

print(data)