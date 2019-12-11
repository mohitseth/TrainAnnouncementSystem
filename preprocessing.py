import os
import pandas as pd
from playsound import playsound
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateAnnouncement(fcity,via,to,train_no,train_name,platform):
        # if(os.path.isfile('2_hindi.mp3')):
        #     os.remove("2_hindi.mp3")
        # if(os.path.isfile('4_hindi.mp3')):
        #     os.remove("4_hindi.mp3")
        # if(os.path.isfile('6_hindi.mp3')):
        #     os.remove("6_hindi.mp3")
        # if(os.path.isfile('8_hindi.mp3')):
        #     os.remove("8_hindi.mp3")
        # if(os.path.isfile('10_hindi.mp3')):
        #     os.remove("10_hindi.mp3")
        textToSpeech(fcity, '2_hindi.mp3')

        # 4 - Generate via-city
        textToSpeech(via, '4_hindi.mp3')

        # 6 - Generate to-city
        textToSpeech(to, '6_hindi.mp3')

        # 8 - Generate train no and name
        textToSpeech(str(train_no)+ " " + str(train_name), '8_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(platform, '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{train_no}.mp3", format="mp3")    