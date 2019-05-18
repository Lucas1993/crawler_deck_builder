#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fragments
import re
import json


def build_boss(data):
    card = fragments.create_template_boss(data['treasure'])
    fragments.place_image_boss(card, data['id'])
    fragments.write_description_boss(card, data['desc'])
    fragments.write_title_boss(card, data['name'], data['subtitle'])
    fragments.write_exp_boss(card, data['stats'])
    return card


def build_hero(data):
    type = 1
    if "Epic" in data['subtitle']:
        type = 2
    card = fragments.create_template_hero(type)
    list_f = ["elfstar", "danae", "lone", "megan", "lady", "gaimina", "roberta"]
    female = any(word in data['desc'].lower() for word in list_f)
    types = re.sub("[^\w]", " ",  data['treasure'].lower()).split()
    tp = "cleric" if len(types) == 0 else types[0]
    fragments.place_image_hero(card, data['id'], tp, female)
    fragments.write_title_hero(card, data['name'], data['subtitle'])
    fragments.write_description_hero(card, data['desc'])
    fragments.place_hero_type(card, types)
    fragments.write_heart(card, data['stats'])
    fragments.place_min_players(card, data['min']) # Trocar star no json
    return card


def build_spell(data):
    card = fragments.create_template_spell()
    fragments.place_image_spell(card, data['id'])
    fragments.write_description_spell(card, data['desc'])
    fragments.write_title_spell(card, data['name'])
    types = re.sub("[^\w]", " ",  data['stats'].lower()).split()
    fragments.place_spell_type(card, types)
    return card


def build_room(data):
    types = re.sub("[^\w]", " ",  data['treasure']).split()
    card = fragments.create_template_room(types)
    fragments.place_image_room(card, data['id'], data['subtitle'].lower())
    fragments.write_description_boss(card, data['desc'])
    fragments.write_title_boss(card, data['name'], data['subtitle'])
    fragments.place_room_type(card, data['subtitle'].lower())
    if data['stats'] == "0":
        fragments.write_heart(card, "0")
    else:
        fragments.write_heart(card, "-" + data['stats'])
    fragments.place_treasure(card, types)
    return card

def build_item(data):
    card = fragments.create_template_item()
    fragments.place_image_item(card, data['id'])
    fragments.write_description_item(card, data['desc'])
    fragments.write_title_item(card, data['name'])
    fragments.place_item_type(card, data['treasure'].lower())
    fragments.place_icon_item(card, data['id'])
    return card

# str  = "{\"amnt\": \"1\", \"subtitle\": \"-\", \"name\": \"Meddling Kids!\", \"min\": \"-\", \"img_url\": \"https://vignette.wikia.nocookie.net/bossmonster/images/f/fd/Meddling_Kids%21.jpg/revision/latest/scale-to-width-down/220?cb=20160505214059\", \"treasure\": \"-\", \"link\": \"/wiki/Meddling_Kids!\", \"stats\": \"Build & Adventure\", \"type\": \"Spell\", \"id\": \"TNL062\", \"desc\": \"Choose a Room. Until the end of turn, it has no ability text. OR Choose a player. If three or more Heroes entered that player's dungeon this turn, that player cannot win this turn.\"}"

# str = "{\"amnt\": \"1\", \"subtitle\": \"Cleric Item\", \"name\": \"Inquisitor's Robes\", \"min\": \"-\", \"img_url\": \"https://vignette.wikia.nocookie.net/bossmonster/images/5/5f/Pic1844159.jpg/revision/latest/scale-to-width-down/300?cb=20140204052205\", \"treasure\": \"Cleric\", \"link\": \"/wiki/Inquisitor%27s_Robes\", \"stats\": \"-\", \"type\": \"Item\", \"id\": \"THK003\", \"desc\": \"Power-Up| Destroy the first Advanced Room that this Hero survives.|Reward| Choose and destroy an Advanced Room in any dungeon.\"}"


# str = "{\"amnt\": \"2\", \"subtitle\": \"Trap Room\", \"name\": \"Lost Library\", \"min\": \"-\", \"img_url\": \"https://vignette.wikia.nocookie.net/bossmonster/images/4/47/Lost_Library.PNG/revision/latest/scale-to-width-down/220?cb=20150506210419\", \"treasure\": \"Mage*2\", \"link\": \"/wiki/Lost_Library\", \"stats\": \"1\", \"type\": \"Room\", \"id\": \"TNL032\", \"desc\": \"You may destroy this Room to draw two Spell cards, then discard a Spell card.\"}"

# str = "{\"amnt\": \"1\", \"subtitle\": \"Epic Hybrid Hero\", \"name\": \"Archer\", \"min\": \"*\", \"img_url\": \"https://vignette.wikia.nocookie.net/bossmonster/images/d/de/Archer.PNG/revision/latest/scale-to-width-down/220?cb=20150506025822\", \"treasure\": \"Fighter / Thief\", \"link\": \"/wiki/Archer\", \"stats\": \"12\", \"type\": \"Hero\", \"id\": \"TNL112\", \"desc\": \"This Hero skips the last Room of your dungeon.\"}"


# str = "{\"amnt\": \"1\", \"subtitle\": \"Vampire Baroness\", \"name\": \"Belladonna\", \"min\": \"-\", \"img_url\": \"https://vignette.wikia.nocookie.net/bossmonster/images/9/98/BM2_Belladonna_fixed.png/revision/latest/scale-to-width-down/346?cb=20150327102020\", \"treasure\": \"Cleric\", \"link\": \"/wiki/Belladonna\", \"stats\": \"350\", \"type\": \"Boss\", \"id\": \"TNL002\", \"desc\": \"Level Up: Heal a Wound. (Turn one face-down Hero face-up.)\"}"

# data = json.loads(str)

def main():
    card = build_item(data)
    card.show()

if __name__ == "__main__":
    main()
