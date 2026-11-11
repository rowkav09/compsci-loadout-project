from __future__ import annotations

from dataclasses import asdict

from PySide6.QtCore import QObject, Slot

from services.skins_repository import SkinsRepository


class SkinsController(QObject):
    """QObject bridge exposing SkinsRepository to QML."""

    def __init__(self, repository: SkinsRepository | None = None, parent=None):
        super().__init__(parent)
        self._repository = repository or SkinsRepository()

    @Slot(str, str, str, str, result="QVariantList")
    def search(self, name: str, finish: str, rarity: str, crate: str) -> list[dict]:
        skins = self._repository.list_skins(
            name=name or None,
            finish=finish or None,
            rarity=rarity or None,
            crate=crate or None,
        )
        return [asdict(skin) for skin in skins]

    @Slot(str, str, str, str, result="QVariantList")
    def search_text(self, query: str, weapon_name: str, rarity: str, crate: str) -> list[dict]:
        skins = self._repository.list_skins(
            name=weapon_name or None,
            rarity=rarity or None,
            crate=crate or None,
        )
        normalized_query = query.strip().casefold()
        if normalized_query:
            skins = [
                skin
                for skin in skins
                if normalized_query in skin.name.casefold()
                or normalized_query in (skin.weapon_name or "").casefold()
            ]
        return [asdict(skin) for skin in skins]

    @Slot(result="QVariantList")
    def weapon_names(self) -> list[str]:
        return self._repository.list_weapon_names()

    @Slot(str, result="QVariantList")
    def finishes(self, weapon_name: str) -> list[str]:
        weapon_id = self._repository.get_weapon_id(weapon_name) if weapon_name else None
        return self._repository.list_finishes(weapon_id)

    @Slot(result="QVariantList")
    def rarities(self) -> list[str]:
        return self._repository.list_rarities()

    @Slot(result="QVariantList")
    def crates(self) -> list[str]:
        return self._repository.list_crates()
