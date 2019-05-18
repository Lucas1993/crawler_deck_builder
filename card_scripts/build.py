#!/usr/bin/env python
# -*- coding: utf-8 -*-
import create_card
import json

######### Main 63mmX88mm -- a4 = 210x297
def main():
    jl_path = "./resources/hidden_secrets.jl"
    with open(jl_path) as f:
        for line in f:
            data = json.loads(line)
            print("Building " + data['id'] + "\n")
            if "Boss" in data['type']:
                card = create_card.build_boss(data)
            elif "Hero" in data['type']:
                card = create_card.build_hero(data)
            elif "Room" in data['type']:
                card = create_card.build_room(data)
            elif "Spell" in data['type']:
                card = create_card.build_spell(data)
            elif "Item" in data['type']:
                card = create_card.build_item(data)
            else:
                print("\n\nERRO " + data['id'] + "\n\n")
            # card.show()
            card.save("./out/" + data['id'] + ".png")


if __name__ == "__main__":
    main()
