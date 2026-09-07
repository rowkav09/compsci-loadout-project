from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Skin:
    id: str
    name: str
    weapon_name: str | None
    weapon_id: int | None
    finish: str
    rarity: str
    crates: tuple[str, ...]

    @classmethod
    def from_raw(cls, raw: dict) -> Skin:
        weapon = raw.get("weapon") or {}
        pattern = raw.get("pattern") or {}
        rarity = raw.get("rarity") or {}
        crates = raw.get("crates") or []
        return cls(
            id=raw.get("id", ""),
            name=raw.get("name", ""),
            weapon_name=weapon.get("name"),
            weapon_id=weapon.get("weapon_id"),
            finish=pattern.get("name") or "Vanilla",
            rarity=rarity.get("name") or "Unknown",
            crates=tuple(crate.get("name") for crate in crates if crate.get("name")),
        )
