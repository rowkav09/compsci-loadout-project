"""Unit tests for the QML-facing SkinsController bridge.

Uses the small sample fixture rather than the full skins.json dataset so
the tests stay fast; dataset-level checks live in test_dataset.py.
"""

from pathlib import Path

import pytest

from controller import SkinsController
from services.skins_repository import SkinsRepository

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "sample_skins.json"


@pytest.fixture
def controller():
    return SkinsController(repository=SkinsRepository(skins_path=FIXTURE_PATH))


def test_search_returns_plain_dicts_for_qml(controller):
    results = controller.search("AK-47", "", "", "")
    assert results, "expected fixture AK-47 results"
    assert all(isinstance(item, dict) for item in results)
    assert {item["id"] for item in results} == {
        "skin-ak-redline",
        "skin-ak-vulcan",
        "skin-ak-vanilla",
    }


def test_search_applies_filters(controller):
    results = controller.search("AK-47", "Redline", "", "")
    assert [item["id"] for item in results] == ["skin-ak-redline"]


def test_search_unknown_weapon_returns_empty_list(controller):
    assert controller.search("Not A Weapon", "", "", "") == []


def test_weapon_names_sorted(controller):
    names = controller.weapon_names()
    assert names == sorted(names)
    assert "AK-47" in names


def test_finishes_scoped_to_weapon(controller):
    assert controller.finishes("AK-47") == ["Redline", "Vanilla", "Vulcan"]


def test_finishes_without_weapon_returns_all(controller):
    assert controller.finishes("") == ["Howl", "Redline", "Vanilla", "Vulcan"]


def test_rarities(controller):
    assert controller.rarities() == ["Classified", "Consumer Grade", "Contraband", "Covert"]


def test_crates(controller):
    assert controller.crates() == ["Huntsman Case", "Operation Phoenix Weapon Case"]
