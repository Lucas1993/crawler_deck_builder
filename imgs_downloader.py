#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib

def main():
    jl_path = "./items_data.jl"
    with_img = 0
    no_img = []
    with open(jl_path) as f:
        for line in f:
            j_content = json.loads(line)
            if j_content['img_url']:
                urllib.urlretrieve(j_content['img_url'], "./cards_dir/" +
                        j_content['id'] + ".jpg")
                print(j_content['id'] + ": done\n")
                with_img = with_img + 1
            else:
                print(j_content['id'] + ": no img\n")
                no_img.append(j_content['id'])
    print("With img: " + str(with_img)) # 71
    print("No img: " + str(len(no_img))) # 43

if __name__ == "__main__":
    main()
