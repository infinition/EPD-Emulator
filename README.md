# EPD-Emulator

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/infinition)

A Python emulator for E-Paper Display (EPD) screens. Renders the display output in a Tkinter window or a Flask web server so you can develop and test EPD code without the physical hardware.

![EPD-Emulator demo](https://github.com/infinition/EPD-Emulator/assets/37984399/6006d07a-e760-46c8-9ded-731a590179f0)

---

## Features

- Tkinter (GUI window) or Flask (browser) rendering, switchable per session.
- Color and monochrome display support.
- Configurable via JSON files for different EPD models.
- Normal and reverse orientation modes.
- Configurable refresh interval.

---

## Supported models (excerpt)

`epd2in13`, `epd2in9`, `epd4in2`, `epd5in83`, `epd6in2`, `epd7in5`, `epd9in7`, `epd10in3`, `epd11in6`, `epd12in48`

---

## Installation

```bash
git clone https://github.com/infinition/EPD-Emulator.git
cd EPD-Emulator
pip install -r requirements.txt
```

Requirements: `Pillow`, `Flask`, `tk`.

---

## Usage

The emulator is called from your own script, not run directly. A demo is included:

```bash
python "waveshare_emulator demo.py"
```

In your script, initialize the emulator:

```python
import epdemulator

epd = epdemulator.EPD(
    config_file="epd2in13",
    use_tkinter=True,
    use_color=False,
    update_interval=0.5,
    reverse_orientation=False
)
```

Parameters:

| Parameter | Description |
|-----------|-------------|
| `config_file` | EPD model name (no extension) |
| `use_tkinter` | `True` for GUI window, `False` for Flask |
| `use_color` | `True` for color display, `False` for monochrome |
| `update_interval` | Screen refresh delay in seconds |
| `reverse_orientation` | `True` to flip the display |

---

## Star History

<a href="https://www.star-history.com/?repos=infinition%2FEPD-Emulator&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=infinition/EPD-Emulator&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=infinition/EPD-Emulator&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=infinition/EPD-Emulator&type=date&legend=top-left" />
 </picture>
</a>

---

## License

MIT. See [LICENSE](LICENSE).
