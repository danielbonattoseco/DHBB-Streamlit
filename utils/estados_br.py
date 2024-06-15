import json

def estados_br():
    with open("dicts/estados_br.json") as f:
        estados_br = json.load(f)
        return estados_br.values()