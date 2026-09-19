"""Integrity checks over the real skins.json dataset shipped in the repo.

These guard the data the whole app queries: if the dataset is truncated,
duplicated, or malformed, the app breaks even when the code is correct.
"""

from item_definition_indexes import weapons
from services.skins_repository import SkinsRepository


def test_dataset_loads_with_expected_minimum_size():
    repo = SkinsRepository()
    # 2092 entries at time of writing; floor guards against truncation.
    assert len(repo.list_skins()) > 1000


def test_dataset_ids_are_unique_and_present():
    repo = SkinsRepository()
    ids = [skin.id for skin in repo.list_skins()]
    assert all(ids)
    assert len(ids) == len(set(ids))


def test_dataset_core_fields_populated():
    repo = SkinsRepository()
    for skin in repo.list_skins():
        assert skin.name
        assert skin.finish
        assert skin.rarity


def test_weapon_index_names_resolve_round_trip():
    repo = SkinsRepository()
    for _, weapon_name, *_ in weapons:
        assert repo.get_weapon_id(weapon_name) is not None


def test_list_helpers_return_sorted_unique_values():
    repo = SkinsRepository()
    for values in (repo.list_weapon_names(), repo.list_rarities(), repo.list_crates()):
        assert values == sorted(values)
        assert len(values) == len(set(values))
