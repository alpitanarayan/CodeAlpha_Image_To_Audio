import pyttsx3
from tkinter import *
text_speech = pyttsx3.init()
user_input_text = input("Please write a paragraph that you want to convert it into speech :")
text_speech.say(user_input_text)
text_speech.runAndWait()


