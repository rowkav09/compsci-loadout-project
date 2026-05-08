import requests
import tabulate
from item_definition_indexes import weapons
import json

headers = {
}
params = {
    'weapon_id': '507'
    
}


# try:
#     data = requests.get(
#         'https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/skins.json',
#         headers=headers,
#         params=params,
#         )
#     data.raise_for_status()
#     data = data.json()
# except requests.RequestException as e:
#     print(f'Failed to fetch listings: {e}')


with open('data.json', 'r') as file:
    data = json.load(file)
def get_id(name):
    for item in weapons:
        if item[1].lower() == name.lower():
            return item[0]
    return('ivalid item name')
        




def get_info(name,finish,rarity,crate_n):
    filtered = [
        skin for skin in data
        if skin.get('weapon', {}).get('weapon_id') == 507
    ]
    tabulated = [['item','rarity','case']]

    for skin in filtered:
        
        if finish and name:
            name = f'{(skin.get('weapon') or {}).get('name')==name} | {(skin.get('pattern') or {}).get('name')==finish}'
        elif finish:
            name = f'{(skin.get('weapon') or {}).get('name')} | {(skin.get('pattern') or {}).get('name')==finish}'
        elif name:
            name = f'{(skin.get('weapon') or {}).get('name')==name} | {(skin.get('pattern') or {}).get('name')}'
        else:
            name = f'{(skin.get('weapon') or {}).get('name')} | {(skin.get('pattern') or {}).get('name')}'
        
        if rarity:
            rarity = f'{(skin.get('rarity') or {}).get('name')==rarity}'
        else:
            rarity = f'{(skin.get('rarity') or {}).get('name')==rarity}'
            
        crate = skin.get('crates') or []
        if crate:
            for item in crate:
                crate_name = crate.get('name')==crate_n if crate else None
        else:
            crate_name = crate[0].get('name') if crate else None
        info = [name,rarity,crate_name]
        tabulated.append(info)

    final = []
    for item in tabulated:
        if item not in final:
            final.append(item)


    print(tabulate.tabulate(final))

