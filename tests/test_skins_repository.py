from pathlib import Path

import pytest

from services.skins_repository import SkinsRepository

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "sample_skins.json"


@pytest.fixture
def repo():
    return SkinsRepository(skins_path=FIXTURE_PATH)


def test_get_weapon_id_known_name(repo):
    assert repo.get_weapon_id("AK-47") == 7


def test_get_weapon_id_is_case_insensitive(repo):
    assert repo.get_weapon_id("ak-47") == 7


def test_get_weapon_id_unknown_name(repo):
    assert repo.get_weapon_id("Not A Weapon") is None


def test_list_skins_by_name_returns_all_matching_weapon(repo):
    results = repo.list_skins(name="AK-47")
    assert {skin.id for skin in results} == {
        "skin-ak-redline",
        "skin-ak-vulcan",
        "skin-ak-vanilla",
    }


def test_list_skins_unknown_name_returns_empty(repo):
    assert repo.list_skins(name="Not A Weapon") == []


def test_list_skins_by_finish(repo):
    results = repo.list_skins(name="AK-47", finish="Redline")
    assert [skin.id for skin in results] == ["skin-ak-redline"]


def test_list_skins_by_rarity(repo):
    results = repo.list_skins(rarity="Covert")
    assert [skin.id for skin in results] == ["skin-ak-vulcan"]


def test_list_skins_by_crate(repo):
    results = repo.list_skins(crate="Huntsman Case")
    assert {skin.id for skin in results} == {"skin-ak-redline", "skin-m4a4-howl"}


def test_missing_pattern_defaults_to_vanilla(repo):
    vanilla = next(skin for skin in repo.list_skins(name="AK-47") if skin.id == "skin-ak-vanilla")
    assert vanilla.finish == "Vanilla"


def test_list_weapon_names_includes_known_weapons(repo):
    names = repo.list_weapon_names()
    assert "AK-47" in names
    assert "M4A4" in names


def test_list_finishes_scoped_to_weapon(repo):
    assert repo.list_finishes(weapon_id=7) == ["Redline", "Vanilla", "Vulcan"]


def test_list_rarities(repo):
    assert repo.list_rarities() == ["Classified", "Consumer Grade", "Contraband", "Covert"]


def test_list_crates(repo):
    assert repo.list_crates() == ["Huntsman Case", "Operation Phoenix Weapon Case"]
