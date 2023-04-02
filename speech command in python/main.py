import kivy
from kivy.uix.gridlayout import GridLayout

import functions

kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.button import Button


def fun():
    text = (functions.voice_RECORDER())
    if text[:6] == "search":
        functions.searche(text[7:])
    else:
        try:
            ano = (functions.search_in_dataset(text))
            functions.playvoice(ano)
        except:
            print("unknown command")


Config.set('graphics', 'resizable', True)




if __name__ == '__main__':
    try:
        text = "blank"
        while text != "obama" :
            text = functions.voice_RECORDER()
            if text == "Obama":
                functions.PopupExample().run()

    except:
        print("nothing was said")

