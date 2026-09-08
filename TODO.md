# TODO

## Controller (next up)

- [x] `SkinsController(QObject)` wrapping a `SkinsRepository` instance (`controller.py`)
- [x] `@Slot` method `search(name, finish, rarity, crate)` returning plain dicts (not `Skin` objects) for QML
- [x] `@Slot` methods for dropdown data: `weapon_names()`, `finishes(weapon_id)`, `rarities()`, `crates()`
- [ ] Register it in `main.py` via `engine.rootContext().setContextProperty("controller", controller)` before `engine.load(...)`
- [ ] Wire the pages under `Ui/UiContent/pages/` to call `controller.search(...)` etc. instead of the static sample `ListModel`s they use now
- [ ] Add unit tests for `SkinsController` (needs `PySide6` in the test env)

## Backend / data, later

- [ ] CSFloat pricing lookups — must run off the GUI thread (`QThread`/`QRunnable` + `Signal`), never a plain synchronous `requests.get` in a `@Slot`
- [ ] Steam inventory import
- [ ] Sort/filter owned skins by price, float, category

## Repo / DevOps

- [ ] Enable branch protection on `main` in GitHub settings (require the CI check, require a PR before merge) — can't be done from code
- [ ] Decide what happens to `gui/Nucleon/` (old Tkinter framework experiment) — archive it properly or delete it
- [ ] Decide what happens to `qml/` (pre-Design-Studio prototype, superseded by `Ui/UiContent/`) — archive or delete it

## UI

- [x] Nav shell (`Ui/UiContent/App.qml`) switching between Loadout Generator / Manual Search / Settings pages
- [x] Reusable components under `Ui/UiContent/components/` (`NavRail`, `PageHeader`, `SectionPanel`, `SkinCard`)
- [x] Basic layout for all three pages, using static sample data (kept plain/unstyled for now)
- [ ] Swap each page's sample data for live `controller` calls once the controller is registered
- [ ] Actual visual design pass once the barebones layout is approved
