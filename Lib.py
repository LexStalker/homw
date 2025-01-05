from PIL import Image
from PIL import ImageDraw, ImageFont



def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))

im = new_photo("oboi_priroda.jpg")
im_2 = new_photo("images.png")


im.paste(im_2, (100, 430))

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("Tiny5-Regular.ttf", 40)
draw.text((100, 100), 'GANDON', font=font, fill="Green" )

im.show()
