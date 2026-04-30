import requests
import tabulate
headers = {
}
params = {
    'weapon_id': '507'
    
}


try:
    data = requests.get(
        'https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/skins.json',
        headers=headers,
        params=params,
        )
    data.raise_for_status()
    data = data.json()
except requests.RequestException as e:
    print(f'Failed to fetch listings: {e}')



filtered = [
    skin for skin in data
    if skin.get('weapon', {}).get('weapon_id') == 507
]
tabulated = [['item','rarity','case']]

for skin in filtered:
    name = f'{(skin.get('weapon') or {}).get('name')} | {(skin.get('pattern') or {}).get('name')}'
    rarity = f'{(skin.get('rarity') or {}).get('name')}'
    crate = skin.get('crates') or []
    crate_name = crate[0].get('name') if crate else None
    info = [name,rarity,crate_name]
    tabulated.append(info)
final = []
for item in tabulated:
    if item not in final:
        final.append(item)


print(tabulate.tabulate(final))

