from gtts import gTTS  # we have imported this module for text to speech conversion
import os
import wave
from pygame import mixer  # Load the popular external library

# if you want from file that you can change this
abc = open('sample.txt')
text = abc.read() #Hello guys, how are you All Fine ?

language = "en"  #en is english language

obj = gTTS(text = text, lang=language, slow = False)
# we have used slow = False because our converted video will have a high speed
obj.save("sample.mp3")
os.system("sample.mp3")