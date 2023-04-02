# import speech_recognition as sr
# from os import path
# from pydub import AudioSegment
#
# # convert mp3 file to wav
# sound = AudioSegment.from_mp3("transcript.mp3")
# sound.export("transcript.wav", format="wav")
#
#
# # transcribe audio file
# AUDIO_FILE = "transcript.wav"
#
# # use the audio file as the audio source
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source)  # read the entire audio file
#
#         print("Transcription: " + r.recognize_google(audio))
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    'app': 'tb://...',
    'version': '13.0',
    'deviceName': 'Pixel 6a',
    'platformName': 'Android'
    }

driver = webdriver.Remote("http://key:secret@localhost:4445/wd/hub", desired_caps)

inputA = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
)
inputA.send_keys("10")

inputB = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputB"))
)
inputB.send_keys("5")

driver.quit()