# iPod MP3 Renamer

This is a simple Python script that renames `.mp3` files copied from an iPod (e.g. iPod Nano) based on their ID3 tags.  
It extracts the artist and title and renames each file to the format:


If a file with the same name already exists, a number will be added to make it unique (e.g. `Artist – Title (1).mp3`).

## Use Case

When copying music files from an iPod to your computer, the filenames are often cryptic (e.g. `AXYZ.mp3`) and scattered across folders like `F00`, `F01`, etc.  
This script scans all `.mp3` files in the given folder and its subfolders, reads their metadata, and saves them back with human-readable names.

---

## Features

- Recursively searches all subfolders (e.g. `F00`, `F01`…)
- Extracts metadata using ID3 tags
- Renames files to `Artist – Title.mp3`
- Automatically handles duplicate names
- Leaves renamed files in the specified folder

---

## Requirements

- Python 3.6+
- [mutagen](https://mutagen.readthedocs.io/en/latest/) library

Install with:

```bash
pip install mutagen
