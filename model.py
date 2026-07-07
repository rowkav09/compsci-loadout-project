from item_definition_indexes import weapons
import json
from tabulate import tabulate
import requests
from config import CSFLOAT_API_KEY


headers = {
    "Authorization": CSFLOAT_API_KEY
}

from test_skins_json_api import get_id
class Skins:
    def __init__(self, data):
        self.data = data
        with open('skins.json', 'r', encoding='utf-8') as file:
            self.data = json.load(file)
    def get_id(self, name):
        for item in self.data:
            if item[1].lower() == name.lower():
                return item[0]
        return 'invalid item name'
    def get_info(self, name=None, finish=None, rarity=None, crate_n=None, weapon_id=None, url=False, price=False):
        
        # default: return all data that mataches the filters: name, finish, rarity, crate_n, weapon_id
        # url: return only the url of the skins that match the filters
        # price: return only the price of the skins that match the filters
        
        # convert weapon name to id
        if weapon_id is None and name is not None:
            if name:
                weapon_id = self.get_id(name)
            else:
                print('Please provide a weapon name or weapon id')
                return

        # invalid name check
        if isinstance(weapon_id, str):
            print('Invalid weapon name')
            return

        if weapon_id is not None:
            filtered = [
                skin for skin in self.data
                if skin.get('weapon', {}).get('weapon_id') == weapon_id
            ]
        else:
            filtered = self.data

        table = [['Item', 'Finish', 'Rarity', 'Case']]

        for skin in filtered:

            weapon_name = (skin.get('weapon') or {}).get('name')
            pattern_name = (skin.get('pattern') or {}).get('name')
            rarity_name = (skin.get('rarity') or {}).get('name')

            pattern_name = pattern_name if pattern_name is not None else "Vanilla"

            # finish filter
            if finish and pattern_name.lower() != finish.lower():
                continue

            # rarity filter
            if rarity and rarity_name.lower() != rarity.lower():
                continue

            crates = skin.get('crates') or []

            # FIXED CASE LOGIC
            if crates:
                crate_names = [
                    crate.get('name')
                    for crate in crates
                    if crate.get('name')
                ]

                # crate filter
                if crate_n:
                    if not any(
                        name.lower() == crate_n.lower()
                        for name in crate_names
                    ):
                        continue

                crate_name = ", ".join(crate_names)
            else:
                crate_name = "Collection"
            count = 0
            table.append([
                weapon_name,
                pattern_name,
                rarity_name,
                crate_name
            ])

        print(tabulate.tabulate(table, headers='firstrow', tablefmt='rounded_grid'))
    def from_weapon_name(self, name):
                self.get_info(name=name)
    def from_weapon_id(self, weapon_id):
                self.get_info(weapon_id=weapon_id)
    def from_weapon_name_and_finish(self, name, finish):
                self.get_info(name=name, finish=finish)
    def from_weapon_name_and_rarity(self, name, rarity):
                self.get_info(name=name, rarity=rarity)
    def from_weapon_name_and_crate(self, name, crate_n):
                self.get_info(name=name, crate_n=crate_n)
    def from_weapon_finish(self, finish):
                self.get_info(finish=finish)
    def from_weapon_rarity(self, rarity):
                self.get_info(rarity=rarity)
    def define_float_category(self, float_value):
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


