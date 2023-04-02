from googlesearch import search
import speech_recognition as sr
import json
import os
import pandas as pd
import glob
from gtts import gTTS
import kivy
from kivy.uix.gridlayout import GridLayout


kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.button import Button




def searche(input_text):
    listof = []
    for j in search(input_text, tld="co.in", num=10, stop=10, pause=2):
        listof.append(j)
        print(j)
    return listof


def voice_RECORDER():
    r = sr.Recognizer()
    s = 1

    while s != 2:
        # Record audio from microphone
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            texting = r.recognize_google(audio)
        try:
            # Convert audio to text
            text = r.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        s += 1

    return texting


def search_in_dataset(input_text):
    # path_to_json = 'english/'
    # json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    # for x in json_files:
    #     file = json.load(x)
    #     for i in file["ai"]:
    #         if input_text.upper() == i[0].upper():
    #            print(i[1])
    #            break
    #         else:
    #            print("did not understand")

    # file = open("english/")
    # data = json.load(file)
    # for i in data["ai"]:
    #   if input_text.upper() == i[0].upper():
    #      print(i[1])
    #     break
    # else:
    #   print("did not understand")

    #    file.close()
    path_to_json = r'english/'
    # import all files from folder which ends with .json
    json_files = glob.glob(os.path.join(path_to_json, '*.json'))

    # convert all files to datafr`enter code here`ame
    df = pd.concat((pd.read_json(f) for f in json_files))
    #   print(df.head())
    name_of_files = []
    global text
    for i in df:
        name_of_files.append(i)
    b = 0
    for j in json_files:
        s = open(j)
        data = json.load(s)

        try:
            for x in data[name_of_files[b]]:
                if input_text.upper() == x[0].upper():
                    print(x[1])
                    text = x[1]
                    break



        except:
            print("unknown error")
        b += 1
    return text


def playvoice(input_text):
    # The text that you want to convert to audio
    mytext = input_text

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system("welcome.mp3")


# Make an app by deriving from the kivy provided app class
class PopupExample(App):
    # override the build method and return the root widget of this App

    def build(self):
        # Define a grid layout for this App
        self.layout = GridLayout(cols=1, padding=10)

        # Add a button
        self.button = Button(text="Click and talk")
        self.layout.add_widget(self.button)

        # Attach a callback for the button press event
        self.button.bind(on_press=self.onButtonPress)

        return self.layout

    # On button press - Create a popup dialog with a label and a close button
    def onButtonPress(self, button):

        layout = GridLayout(cols=1, padding=10)
        text = (voice_RECORDER())
        if text[:6] == "search":
            returning = (searche(text[7:]))
            x = 0
            for i in returning:
                pupuplabel = Label(text=f" {x} : " + returning[x])
                layout.add_widget(pupuplabel)
                x += 1
        else:
            try:
                ano = (search_in_dataset(text))
                pupuplabele = Label(text=ano)
                layout.add_widget(pupuplabele)

                playvoice(ano)
            # tts.speak(message=ano)

            except:
                print("unknown command")

        popupLabel = Label(text="you said:  " + text)
        closeButton = Button(text="Close the pop-up")

        layout.add_widget(popupLabel)

        layout.add_widget(closeButton)

        # Instantiate the modal popup and display
        popup = Popup(title=' my own siri',
                      content=layout)
        popup.open()

        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press=popup.dismiss)
