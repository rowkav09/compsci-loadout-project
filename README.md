# CS2 Loadout Generator

A work-in-progress A-Level Computer Science project for browsing and filtering Counter-Strike 2 weapon skins. The project pairs a Python backend with a PySide6/QML desktop interface.

> **Project status:** Work in progress. The interface is a prototype and the skin-search functionality is under active development.

## Features

- Load and query local CS2 skin data from `skins.json`
- Filter skins by weapon, finish, rarity, or case/collection
- Convert float values into CS2 wear categories
- Desktop UI built with PySide6/QML

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

## Optional API configuration

`config.py` reads the following values from your environment (or a local `.env` file):

```env
CSFLOAT_API_KEY=your_key_here
BUFF_API_KEY=your_key_here
STEAM_API_KEY=your_key_here
```

Do not commit credentials or `.env` files.

## Roadmap

- [x] Filter AK-47 skins using selectable parameters
- [ ] Build a full loadout from a user's Steam inventory
- [ ] Sort and filter owned skins by price, float, and category
- [ ] Expand the prototype UI into a complete loadout-building experience

See [TODO.md](TODO.md) for the current working task list.

## Contributing

This is an in-progress coursework project. Pull requests go through CI (lint + tests) before merging into `main`.

## License

No license has been added yet. All rights are reserved unless the project owner adds a license file.
