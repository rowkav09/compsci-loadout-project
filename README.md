# CS2 Loadout Generator

A work-in-progress A-Level Computer Science project for browsing and filtering Counter-Strike 2 weapon skins. The project pairs a Python data model with a lightweight PySide6/QML desktop interface.

> **Project status:** Work in progress. The current interface is a prototype and the skin-search functionality is under active development.

## Features

- Load and query local CS2 skin data from `skins.json`
- Filter skins by weapon, finish, rarity, or case/collection
- Display matching results in a terminal table
- Convert float values into CS2 wear categories
- Launch a basic PySide6/QML desktop window
- Read optional API credentials from environment variables

## Requirements

- Python 3.10 or newer
- `pip`
- PySide6-compatible desktop environment for the GUI

## Installation

```bash
git clone https://github.com/rowkav09/compsci-loadout-project.git
cd compsci-loadout-project
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the desktop prototype

```bash
python main.py
```

This loads `Main.qml`, which currently provides a simple PySide6/QML proof-of-concept window.

## Working with skin data

The `Skins` class in `model.py` loads `skins.json` and can print filtered skin data to the terminal.

```python
from model import Skins

skins = Skins(data=None)
skins.from_weapon_name("AK-47")
skins.from_weapon_name_and_rarity("AK-47", "Covert")
skins.from_weapon_name_and_finish("AK-47", "Redline")
```

Available filtering helpers include:

- `from_weapon_name(name)`
- `from_weapon_id(weapon_id)`
- `from_weapon_name_and_finish(name, finish)`
- `from_weapon_name_and_rarity(name, rarity)`
- `from_weapon_name_and_crate(name, crate_name)`
- `from_weapon_finish(finish)`
- `from_weapon_rarity(rarity)`

Wear categories are determined with `define_float_category(float_value)`:

| Float range | Category |
| --- | --- |
| `< 0.07` | Factory New |
| `< 0.15` | Minimal Wear |
| `< 0.38` | Field-Tested |
| `< 0.45` | Well-Worn |
| `>= 0.45` | Battle-Scarred |

## Optional API configuration

`config.py` reads the following values from your environment (or a local `.env` file):

```env
CSFLOAT_API_KEY=your_key_here
BUFF_API_KEY=your_key_here
STEAM_API_KEY=your_key_here
```

Do not commit credentials or `.env` files. The current code uses `CSFLOAT_API_KEY` when making authenticated requests.

## Repository layout

```text
main.py                    Application entry point
Main.qml                   Prototype desktop UI
model.py                   Skin data loading, filtering, and wear categorisation
config.py                  Environment-based API configuration
skins.json                 Local CS2 skin data
item_definition_indexes.py Weapon identifier data
requirements.txt           Python dependencies
example/                   Small example and QML support files
```

## Roadmap

- [x] Filter AK-47 skins using selectable parameters
- [ ] Build a full loadout from a user's Steam inventory
- [ ] Sort and filter owned skins by price, float, and category
- [ ] Expand the prototype UI into a complete loadout-building experience

## Contributing

This is an in-progress coursework project. Bug reports and focused pull requests are welcome; please use Conventional Commit-style messages such as `fix: correct rarity filtering` or `docs: clarify setup instructions`.

## License

No license has been added yet. All rights are reserved unless the project owner adds a license file.