from PIL import Image, ImageDraw, ImageFont

img = Image.open("background.png")
draw = ImageDraw.Draw(img)
draw.line((0, 0) + img.size, fill=128)
draw.line((0, img.size[1], img.size[0], 0), fill=128)
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 80)
# draw text, half opacity
draw.text((250,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
draw.text((250,60), "World", font=fnt, fill=(255,255,255,255))
del draw

# write to stdout
img.save("output.png", "PNG")
