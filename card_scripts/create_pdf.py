#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from fpdf import FPDF


start_x = 7
start_y = 7

cur_x = 7
cur_y = 7


def place_card(pdf, id):
    global cur_x
    global cur_y
    global start_x
    global start_y
    if cur_x + 63 > 200:
        if cur_y + 88 + 88 > 287:
            print("new page")
            pdf.add_page() # new page
            cur_x = start_x
            cur_y = start_y
            pdf.image('./vdash.png', cur_x, cur_y - 5, 2)
            pdf.image('./vdash.png', cur_x + 63, cur_y - 5, 2)
            pdf.image('./out/' + id + '.png', cur_x, cur_y, 63)
            print("(" + str(cur_x) + ", " + str(cur_y) + ") -> (" + str(cur_x
                + 63) + ", " + str(cur_y + 88) + ")")
            cur_x = cur_x + 65
        else:
            print("new line")
            cur_y = cur_y + 90 # new line
            cur_x = start_x
            pdf.image('./out/' + id + '.png', cur_x, cur_y, 63)
            print("(" + str(cur_x) + ", " + str(cur_y) + ") -> (" + str(cur_x
                + 63) + ", " + str(cur_y + 88) + ")")
            cur_x = cur_x + 65
    else:
        pdf.image('./out/' + id + '.png', cur_x, cur_y, 63)
        print("(" + str(cur_x) + ", " + str(cur_y) + ") -> (" + str(cur_x
            + 63) + ", " + str(cur_y + 88) + ")")
        cur_x = cur_x + 65
    print("Placing " + id)



######### Main 63mmX88mm -- a4 = 210x297
def main():
    jl_path = "./resources/cards_data.jl"
    data_names = ["cards_data", "items_data", "hidden_secrets"]
    pdf = FPDF()
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    for file_name in data_names:
        with open("./resources/" + file_name + ".jl") as f:
            for line in f:
                data = json.loads(line)
                n = int(data['amnt'])
                for i in range(n):
                    place_card(pdf, data['id'])
    pdf.output('./out/out.pdf', 'F')


if __name__ == "__main__":
    main()
