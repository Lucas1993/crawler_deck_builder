Crawler and deck builder
========================

This is a personal repository for storing a set of scripts used for building my version of the Bossmonster card game.

There are three main parts for this repo:

- The `crawler` folder: a crawler application written in Scrapy that fetches the info for each card from the bossmonster wikia and stores it on a json-lines file.

- The `imgs_downloader.py` file, which fetches the images of each card from the links obtained from the crawler.

- The `create_pdf.py` file, which programmatically build the image for each card, inserting text, icons, descriptions, etc., obtained in the previous steps. It then generates a PDF file with all the cards.

Note that some manual cropping on the images from step 2 may be required, as they do not come in a standard way. For storage reasons, this repository does not contain any images.

