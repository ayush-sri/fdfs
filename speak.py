import pyglet
from gtts import gTTS
import time,os

def tts(text,lang):
    file=gTTS(text = text,lang = lang)
    filename= os.getcwd()+"/temp.mp3"
    file.save(filename)
    music = pyglet.media.load(filename,streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(filename)


