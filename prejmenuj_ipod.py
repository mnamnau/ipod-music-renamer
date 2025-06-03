import os
from pathlib import Path
from mutagen.easyid3 import EasyID3

# Přenositelná cesta – složka "ipod_music" na Ploše uživatele
folder_path = Path.home() / "Desktop" / "ipod_music"

def make_unique_filename(folder, base_name):
    name, ext = os.path.splitext(base_name)
    counter = 1
    new_name = base_name
    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name} ({counter}){ext}"
        counter += 1
    return new_name

print(f"📁 Scanning folder: {folder_path}")
if not folder_path.exists():
    print("❌ Folder does not exist.")
else:
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".mp3"):
                file_path = os.path.join(root, filename)
                try:
                    audio = EasyID3(file_path)
                    artist = audio.get("artist", ["Unknown Artist"])[0]
                    title = audio.get("title", ["Unknown Title"])[0]

                    new_filename = f"{artist} – {title}.mp3"
                    new_filename = "".join(c for c in new_filename if c not in '\\/:*?"<>|')
                    new_filename = make_unique_filename(folder_path, new_filename)

                    new_file_path = os.path.join(folder_path, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f"✅ Renamed: {filename} → {new_filename}")
                except Exception as e:
                    print(f"⚠️  Error with file {filename}: {e}")
