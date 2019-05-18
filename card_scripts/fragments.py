#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFilter
from image_utils import ImageText
import os.path


######### Create template
def create_template_boss(type):
    card = Image.open("./resources/boss_" + type.lower() + ".jpg").convert("RGBA")
    return card


def create_template_hero(type=1):
    if type == 1:
        card = Image.open("./resources/hero_card.png")
    else:
        card = Image.open("./resources/epic_hero_card.png")
    return card


def create_template_spell():
    card = Image.open("./resources/spell_card.png")
    return card


def create_template_room(types):
    if "2" not in types and len(types) > 1:
        card = Image.open("./resources/room_hybrid.png")
    elif "Universal" in types:
        card = Image.open("./resources/room_hybrid.png")
    else:
        card = Image.open("./resources/room_" + types[0].lower() + ".jpg").convert("RGBA")
    return card

def create_template_item():
    card = Image.open("./resources/card_item.png")
    return card


######### Place image
def place_image_boss(card, id):
    path = "./resources/defaults/" + id + ".png"
    if os.path.isfile(path):
        box = Image.open(path).resize((608, 504), Image.ANTIALIAS)
    else:
        box = Image.open("../pink.png").convert("RGBA")
    card.paste(box, (104, 192))

def place_image_room(card, id, type):
    path = "./resources/defaults/" + id + ".png"
    if os.path.isfile(path):
        box = Image.open(path).resize((608, 504), Image.ANTIALIAS)
    else:
        if "monster" in type:
            box = Image.open("./resources/defaults/def_monster.png").convert("RGBA")
        else:
            box = Image.open("./resources/defaults/def_trap.png").convert("RGBA")
    card.paste(box, (104, 192))

def place_image_hero(card, id, type, female=False):
    path = "./resources/defaults/" + id + ".png"
    if os.path.isfile(path):
        box = Image.open(path).resize((590, 422), Image.ANTIALIAS)
    else:
        if female:
            box = Image.open("./resources/defaults/def_" + type
                    +"_f.png").resize((590, 422), Image.ANTIALIAS)
        else:
            box = Image.open("./resources/defaults/def_" + type
                    +".png").resize((590, 422), Image.ANTIALIAS)
    card.paste(box, (114, 270))


def place_image_spell(card, id):
    path = "./resources/defaults/" + id + ".png"
    if os.path.isfile(path):
        box = Image.open(path).resize((540, 398), Image.ANTIALIAS)
    else:
        box = Image.open("./resources/defaults/def_spell.png").convert("RGBA").resize((540, 398), Image.ANTIALIAS)
    card.paste(box, (137, 253))

def place_image_item(card, id):
    path = "./resources/defaults/" + id + ".png"
    box = Image.open(path).resize((587, 375), Image.ANTIALIAS)
    card.paste(box, (115, 235))


######### Write description
def write_description_boss(card, text):
    color = (255, 255, 255)
    font = 'resources/lucida-sans/LucidaSansRegular.ttf'
    img = ImageText((590, 170), background=(255, 255, 255, 0)) # 200 = alpha
    size = 22 if len(text) > 200 else 25
    img.write_text_box((0, 0), text, place='center', box_width=590,
            font_filename=font, font_size=size, color=color)
    card.paste(img.image, (113, 725), img.image)


def write_description_hero(card, text):
    color = (0, 0, 0)
    font = 'resources/lucida-sans/LucidaSansRegular.ttf'
    img = ImageText((565, 170), background=(255, 255, 255, 0)) # 200 = alpha
    size = 22 if len(text) > 200 else 25
    img.write_text_box((0, 0), text.replace("\n", ":"), place='center', box_width=565,
            font_filename=font, font_size=size, color=color)
    card.paste(img.image, (123, 710), img.image)


def write_description_spell(card, text):
    color = (0, 0, 0)
    font = 'resources/lucida-sans/LucidaSansRegular.ttf'
    img = ImageText((470, 200), background=(255, 255, 255, 0)) # 200 = alpha
    size = 25 if len(text) > 100 else 30
    img.write_text_box((0, 0), text, place='center', box_width=470,
            font_filename=font, font_size=size, color=color)
    card.paste(img.image, (174, 675), img.image)

def write_description_item(card, text_whole):
    lines = text_whole.split('|')
    color = (0, 0, 0)
    font = 'resources/lucida-sans/LucidaSansRegular.ttf'
    img = ImageText((475, 160), background=(255, 255, 255, 0)) # 200 = alpha
    size = 22 if len(lines[3]) > 100 else 25
    img.write_text_box((0, 0), lines[3], place='center', box_width=475,
            font_filename=font, font_size=25, color=color)
    card.paste(img.image, (185, 635), img.image)

    size = 22 if len(lines[1]) > 100 else 25
    img = ImageText((420, 150), background=(255, 255, 255, 0)) # 200 = alpha
    img.write_text_box((0, 0), lines[1], place='center', box_width=420,
            font_filename=font, font_size=size, color=(255, 255, 255))
    card.paste(img.image, (180, 850), img.image)


######### Title
def write_title_hero(card, title, subtitle):
    subt_formatted = subtitle.lower().replace(" ", "_")
    subtitle_pic = Image.open("./resources/text_" + subt_formatted + ".png")
    x, y = subtitle_pic.size
    card.paste(subtitle_pic, (380 - x/2, 182), subtitle_pic)
    color = (0, 0, 0)
    font = 'resources/dos/dos.ttf'
    img = ImageText((405, 75), background=(255, 255, 255, 0)) # 200 = alpha
    img.write_text_box((0, 0), title, place='center', box_width=405,
            font_filename=font, font_size=40, color=color)
    card.paste(img.image, (380 - 200, 93), img.image)


def write_title_spell(card, title):
    color = (0, 0, 0)
    font = 'resources/dos/dos.ttf'
    img = ImageText((540, 75), background=(255, 255, 255, 0)) # 200 = alpha
    img.write_text_box((0, 0), title, place='center', box_width=540,
            font_filename=font, font_size=40, color=color)
    card.paste(img.image, (136, 150), img.image)

def write_title_boss(card, title, subtitle):
    color = (255, 255, 255)
    font = 'resources/dos/dos.ttf'
    img = ImageText((690, 160), background=(255, 255, 255, 0)) # 200 = alpha
    img.write_text_box((0, 0), title, place='center', box_width=690,
            font_filename=font, font_size=45, color=color)
    card.paste(img.image, (80, 55), img.image)
    img = ImageText((690, 80), background=(255, 255, 255, 0)) # 200 = alpha
    img.write_text_box((0, 0), subtitle, place='center', box_width=690,
            font_filename=font, font_size=25, color=color)
    card.paste(img.image, (80, 120), img.image)

def write_title_item(card, title):
    color = (0, 0, 0)
    font = 'resources/dos/dos.ttf'
    size = 40 if len(title) < 15 else 30
    img = ImageText((440, 80), background=(255, 255, 255, 0)) # 200 = alpha
    img.write_text_box((0, 0), title, place='center', box_width=440,
            font_filename=font, font_size=size, color=color)
    card.paste(img.image, (255, 90), img.image)

######### Type specific
def place_treasure(card, types):
    if len(types) > 1:
        if "2" not in types:
            ico = Image.open("./resources/icon_" + types[0].lower() +
                    ".png").resize((128, 120), Image.ANTIALIAS)
            card.paste(ico, (520, 908), ico)
            ico = Image.open("./resources/icon_" + types[1].lower() +
                    ".png").resize((128, 120), Image.ANTIALIAS)
            card.paste(ico, (630, 908), ico)
        else:
            ico = Image.open("./resources/icon_" + types[0].lower() +
                    ".png").resize((128, 120), Image.ANTIALIAS)
            card.paste(ico, (500, 905), ico)
    elif "Universal" in types:
            ico = Image.open("./resources/icon_thief.png").resize((128, 120), Image.ANTIALIAS)
            card.paste(ico, (630, 908), ico)
            ico = Image.open("./resources/icon_mage.png").resize((128, 120), Image.ANTIALIAS)
            card.paste(ico, (530, 908), ico)
            ico = Image.open("./resources/icon_fighter.png").resize((128, 120), Image.ANTIALIAS)
            card.paste(ico, (410, 908), ico)
            ico = Image.open("./resources/icon_cleric.png").resize((128, 120), Image.ANTIALIAS)
            card.paste(ico, (295, 908), ico)



def place_room_type(card, room_type):
    if "advanced" in room_type:
        if "monster" in room_type:
            ico = Image.open("./resources/icon_monster_advanced.png")
        else:
            ico = Image.open("./resources/icon_trap_advanced.png")
    else:
        if "monster" in room_type:
            ico = Image.open("./resources/icon_monster.png")
        else:
            ico = Image.open("./resources/icon_trap.png")
    card.paste(ico, (85, 85), ico)


def place_hero_type(card, types):
    formatted = "_".join(sorted(types))
    if bool(formatted):
        type = Image.open("./resources/hero_" + formatted + ".png")
    else:
        type = Image.open("./resources/hero_special.png")

    type = type.resize((167, 167), Image.ANTIALIAS)
    card.paste(type, (559, 87), type)

def place_icon_item(card, id):
    type = Image.open("./resources/defaults/item_" + id + ".png")
    type = type.resize((96, 96), Image.ANTIALIAS)
    card.paste(type, (627, 870))


def place_min_players(card, min):
    if min == "*":
        players = Image.open("./resources/players_star.png")
    elif int(min) > 4:
        players = Image.open("./resources/players_5.png")
    else:
        players = Image.open("./resources/players_" + min + ".png")
    x, y = players.size
    card.paste(players, (425 - x/2, 935), players)


def write_heart(card, number):
    color = (255, 255, 255)
    font = 'resources/dos/dos.ttf'
    img = ImageText((75, 115), background=(255, 255, 255, 0)) # 200 = alpha
    img.write_text_box((0, 0), number, place='center', box_width=75,
            font_filename=font, font_size=60, color=color)
    if int(number) < 0:
        card.paste(img.image, (140, 893), img.image)
    else:
        card.paste(img.image, (143, 893), img.image)


def place_spell_type(card, types):
    type = Image.open("./resources/spell_icon_" + "_".join(sorted(types)) + ".png")
    card.paste(type, (165, 935), type)


def place_item_type(card, type):
    type = Image.open("./resources/item_" + type.lower() + ".png")
    card.paste(type, (117, 97), type)


def write_exp_boss(card, exp):
    color = (255, 255, 255)
    text = exp + ' XP'
    font = 'resources/dos/dos.ttf'
    img = ImageText((220, 100), background=(255, 255, 255, 0))
    img.write_text_box((0, 0), text, place='center', box_width=220,
            font_filename=font, font_size=50, color=color)
    shadow = ImageText((220, 100), background=(255, 255, 255, 0))
    shadow.write_text_box((0, 0), text, place='center', box_width=220,
            font_filename=font, font_size=50, color=(0, 0, 0))
    shadow.image = shadow.image.resize((230,110), Image.ANTIALIAS)
    shadow.image = shadow.image.filter(ImageFilter.BLUR)
    shadow.image = shadow.image.filter(ImageFilter.BLUR)
    card.paste(shadow.image, (90, 895), shadow.image)
    card.paste(img.image, (90, 900), img.image)
