# Development Iterations

This directory contains prototypes, experiments and earlier implementation
approaches created during development of the CS2 Loadout Generator.

They are intentionally retained as evidence of the project's iterative
development process.

## Structure

- `gui/` - GUI embedding and display experiments, including Tkinter and Pygame.
- `image-processing/` - experiments involving item/image parsing and display.
- `qt/` - early Qt / PySide6 experiments.
- `old-gui/` - reserved for earlier GUI implementations that may later be
  archived here without altering their internal structure.
- `api-experiments/` - early CSFloat API scripts exploring price/float filtering,
  superseded by `model.py`.
- `cli-prototypes/` - the original interactive CLI prototype for skin lookup,
  superseded by the `Skins` class in `model.py`.

These files are not part of the final application's main execution path.

The current application is launched from `main.py`, with its Qt Quick interface
stored under `qml/`.

The existing `gui/Nucleon` experiment is deliberately left untouched by this
