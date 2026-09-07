from __future__ import annotations

import json
from pathlib import Path

from item_definition_indexes import weapons
from models.skin import Skin

DEFAULT_SKINS_PATH = Path(__file__).resolve().parent.parent / "skins.json"


class SkinsRepository:
    """Read-only query layer over the local skins.json dataset."""

    def __init__(self, skins_path: Path | str = DEFAULT_SKINS_PATH):
        with open(skins_path, "r", encoding="utf-8") as file:
            raw_skins = json.load(file)
        self._skins = [Skin.from_raw(entry) for entry in raw_skins]

    def get_weapon_id(self, name: str) -> int | None:
        for weapon_id, weapon_name, *_ in weapons:
            if weapon_name.lower() == name.lower():
                return weapon_id
        return None

    def list_weapon_names(self) -> list[str]:
        return sorted({weapon_name for _, weapon_name, *_ in weapons})

    def list_finishes(self, weapon_id: int | None = None) -> list[str]:
        skins = self._skins if weapon_id is None else [s for s in self._skins if s.weapon_id == weapon_id]
        return sorted({skin.finish for skin in skins})

    def list_rarities(self) -> list[str]:
        return sorted({skin.rarity for skin in self._skins})

    def list_crates(self) -> list[str]:
        crates: set[str] = set()
        for skin in self._skins:
            crates.update(skin.crates)
        return sorted(crates)

    def list_skins(
        self,
        *,
        name: str | None = None,
        finish: str | None = None,
        rarity: str | None = None,
        crate: str | None = None,
        weapon_id: int | None = None,
    ) -> list[Skin]:
        if weapon_id is None and name is not None:
            weapon_id = self.get_weapon_id(name)
            if weapon_id is None:
                return []

        results = self._skins
        if weapon_id is not None:
            results = [s for s in results if s.weapon_id == weapon_id]
        if finish is not None:
            results = [s for s in results if s.finish.lower() == finish.lower()]
        if rarity is not None:
            results = [s for s in results if s.rarity.lower() == rarity.lower()]
        if crate is not None:
            results = [s for s in results if any(c.lower() == crate.lower() for c in s.crates)]
        return list(results)
