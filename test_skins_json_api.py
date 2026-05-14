import requests
import tabulate
from item_definition_indexes import weapons
import json
import urllib.request
from PIL import Image
import json

with open('skins.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
def get_id(name):
    for item in weapons:
        if item[1].lower() == name.lower():
            return item[0]
    return('invalid item name')

def get_info(name=None, finish=None, rarity=None, crate_n=None, weapon_id=None):

    # convert weapon name to id
    if weapon_id is None and name is not None:
        if name:
            weapon_id = get_id(name)
        else:
            print('Please provide a weapon name or weapon id')
            return


    # invalid name check
    if isinstance(weapon_id, str):
        print('Invalid weapon name')
        return
    if weapon_id is not None:
        filtered = [
            skin for skin in data
            if skin.get('weapon', {}).get('weapon_id') == weapon_id
        ]
    else:
        filtered = [
            skin for skin in data
        ]

    table = [['Item','|','Finish', 'Rarity', 'Case']]

    for skin in filtered:

        weapon_name = (skin.get('weapon') or {}).get('name')
        pattern_name = (skin.get('pattern') or {}).get('name')
        rarity_name = (skin.get('rarity') or {}).get('name')
        pattern_name = pattern_name if pattern_name is not None else "Vanilla"
        crates = skin.get('crates') or []
        
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
        if crate_name is None:
            crate_name = "Collection"
        #item_name = f'{weapon_name} | {pattern_name}'

        table.append([weapon_name,'|',pattern_name, rarity_name, crate_name])

    print(tabulate.tabulate(table))

def cli():
    valid = True 
    while valid:
        print('1. Get skins by weapon name')
        print('2. Get skins by weapon id')
        print('3. get skins by weapon name and finish')
        print('4. get skins by weapon name and rarity')
        print('5. get skins by weapon name and crate')
        print('6. get skins by weapon finish')
        print('7. get skins by weapon rarity')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter weapon name: ')
            get_info(name=name)
        elif choice == '2':
            weapon_id = int(input('Enter weapon id: '))
            get_info(weapon_id=weapon_id)
        elif choice == '3':
            name = input('Enter weapon name: ')
            finish = input('Enter finish: ')
            get_info(name=name, finish=finish)
        elif choice == '4':
            name = input('Enter weapon name: ')
            rarity = input('Enter rarity: ')
            get_info(name=name, rarity=rarity)
        elif choice == '5':
            name = input('Enter weapon name: ')
            crate_n = input('Enter crate name: ')
            get_info(name=name, crate_n=crate_n)
        elif choice == '6':
            finish = input('Enter finish: ')
            get_info(finish=finish)
        elif choice == '7':
            rarity = input('Enter rarity: ')
            get_info(rarity=rarity)
        else:
            print('Invalid choice')

cli()

# url = 'https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XsnXwtmkJjSU91dh8bj35VTqVBP4io_fr3EVvKD6MKU_cKPKXWHFxLkls7FsSnDqwUl_sWTczoqheHifbwMmD5F1RvlK7Ec_KL6Q_A'
# urllib.request.urlretrieve(
#   url,
#    "gfg.png")

# img = Image.open("gfg.png")
# img.show()