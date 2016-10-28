from PIL import Image, ImageDraw, ImageFont
from sys import argv
import yaml
import Card

def insert_text(text, coordinates, font_size, align, draw_object):
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', font_size)
    if align=="center":
        width=draw_object.textsize(text, font)[0]
        coordinates = (coordinates[0]-width/2, coordinates[1])
    draw_object.multiline_text(coordinates, text, font=font, align=align)
    
def generate_card(card):
    img = Image.open("background.png")
    draw = ImageDraw.Draw(img)
    insert_text(card.title, (320, 10), 80, "center", draw)
    insert_text(card.text, (100, 600), 30, "left", draw)
    del draw
    img.save(card.filename, "PNG")

with open(argv[-1],  "r") as f:
    yml = yaml.load_all(f)
    for card in yml:
        generate_card(card)
