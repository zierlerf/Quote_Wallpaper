__author__ = 'florian'

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from django.conf import settings

from os import path

import textwrap

class ImageCreator():

    def __init__(self,width,height,text,font):
        self.width = width
        self.height = height
        self.text = textwrap.wrap(text, width=20)
        #font_path = path.join("res/fonts",font + ".ttf")
        self.font = ImageFont.truetype(font,80)

    def createImage(self):
        img_width = self.width
        img_height = self.height

        img_size = (img_width,img_height)
        img = Image.new("RGB",img_size)
        draw = ImageDraw.Draw(img)

        img_text = self.text
        img_font = self.font


        t = len(img_text)
        current_h= (img_height / 2) - len(img_text) * 50

        for line in img_text:
            w, h = draw.textsize(line,font=img_font)
            draw.text(((img_width - w)/2,current_h),line,font=img_font)
            current_h += h + 25

        #img.show()
        pic_path = path.join(settings.PICTURES_URL,"pic.png")
        img.save("wallpaper/static/pictures/pic.png","PNG")