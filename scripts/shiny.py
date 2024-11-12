import os
import json
import re

files = os.scandir("../pokemon/shiny")
female_files = os.scandir("../pokemon/shiny/female")
dex = json.load(open("pokedex/pokedex.json", "r"))

for file in files:
    name = file.name
    for entry in dex:
        pattern = r"^{}(?=\.|-)".format(entry["species"])
        match = re.match(pattern, name)
        if match:
            print("new name: ", name.replace(entry["species"], str(entry["pokedex_number"])))
            os.rename(file.path, file.path.replace(entry["species"], str(entry["pokedex_number"])))
            break
        else:
            continue
    continue

for file in female_files:
    name = file.name
    for entry in dex:
        pattern = r"^{}(?=\.|-)".format(entry["species"])
        match = re.match(pattern, name)
        if match:
            print("new name: ", name.replace(entry["species"], str(entry["pokedex_number"])))
            os.rename(file.path, file.path.replace(entry["species"], str(entry["pokedex_number"])))
            break
        else:
            continue
    continue