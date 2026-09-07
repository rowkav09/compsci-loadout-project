# TODO

## Controller (next up)

- [ ] `SkinsController(QObject)` wrapping a `SkinsRepository` instance
- [ ] `@Slot` method `search(name, finish, rarity, crate)` returning plain dicts (not `Skin` objects) for QML
- [ ] `@Slot` methods for dropdown data: `weapon_names()`, `finishes(weapon_id)`, `rarities()`, `crates()`
- [ ] Register it in `main.py` via `engine.rootContext().setContextProperty("controller", controller)` before `engine.load(...)`
- [ ] Build one throwaway QML page that calls `controller.search(...)` just to prove the bridge works end to end

## Backend / data, later

- [ ] CSFloat pricing lookups — must run off the GUI thread (`QThread`/`QRunnable` + `Signal`), never a plain synchronous `requests.get` in a `@Slot`
- [ ] Steam inventory import
- [ ] Sort/filter owned skins by price, float, category

## Repo / DevOps

- [ ] Enable branch protection on `main` in GitHub settings (require the CI check, require a PR before merge) — can't be done from code
- [ ] Decide what happens to `gui/Nucleon/` (old Tkinter framework experiment) — archive it properly or delete it

## UI (once controller works)

- [ ] Replace `qml/Main.qml` prototype with real search/filter page(s) under `qml/pages/`
- [ ] Break out reusable pieces into `qml/components/`
