__author__ = 'florian'

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Quote_Wallpaper.settings")

from wallpaper.models import Font

def insertFonts():
    Font.save(Font(name="Segoe UI",path="res/fonts/Segoe_UI.ttf"))
    Font.save(Font(name="Coneria Script",path="res/fonts/Demo_ConeriaScript.ttf"))

insertFonts()