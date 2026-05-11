import requests
import tabulate
from item_definition_indexes import weapons
import json
import urllib.request
from PIL import Image
import json

headers = {
}
params = {
    'weapon_id': '507'
    
}




with open('skins.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
def get_id(name):
    for item in weapons:
        if item[1].lower() == name.lower():
            return item[0]
    return('ivalid item name')
        




def get_info(name=None, finish=None, rarity=None, crate_n=None, weapon_id=None):

    # convert weapon name to id
    if weapon_id is None:
        if name:
            weapon_id = get_id(name)
        else:
            print('Please provide a weapon name or weapon id')
            return

    # invalid name check
    if isinstance(weapon_id, str):
        print('Invalid weapon name')
        return

    filtered = [
        skin for skin in data
        if skin.get('weapon', {}).get('weapon_id') == weapon_id
    ]

    table = [['item', 'rarity', 'case']]

    for skin in filtered:

        weapon_name = (skin.get('weapon') or {}).get('name')
        pattern_name = (skin.get('pattern') or {}).get('name')
        rarity_name = (skin.get('rarity') or {}).get('name')
        pattern_name = pattern_name if pattern_name is not None else "Vanilla"
        crates = skin.get('crates') or []

        # optional filters
        if pattern_name is not None:
            if finish and pattern_name.lower() != finish.lower():
                continue

        if rarity and rarity_name.lower() != rarity.lower():
            continue

        crate_name = None

        if crates:
            for crate in crates:

                current_crate = crate.get('name')

                # filter by crate
                if crate_n:
                    if current_crate.lower() != crate_n.lower():
                        continue

                crate_name = current_crate
                break

        item_name = f'{weapon_name} | {pattern_name}'

        table.append([item_name, rarity_name, crate_name])

    print(tabulate.tabulate(table))

get_info(name='r8 revolver')

# url = 'https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XsnXwtmkJjSU91dh8bj35VTqVBP4io_fr3EVvKD6MKU_cKPKXWHFxLkls7FsSnDqwUl_sWTczoqheHifbwMmD5F1RvlK7Ec_KL6Q_A'
# urllib.request.urlretrieve(
#   url,
#    "gfg.png")

# img = Image.open("gfg.png")
# img.show()