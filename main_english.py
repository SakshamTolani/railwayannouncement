import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    myText=str(text)
    language="en"
    myObj=gTTS(text=myText,lang=language, slow=False)
    myObj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio=AudioSegment.from_mp3('announcement.mp3')
    # 1-Generating For your kind attention please train number
    start = 20400
    stop = 27000
    audioProcessed = audio[start : stop]
    audioProcessed.export("1_english.mp3", format='mp3')

    # 2-Input train number from excel file

   # 3-Generating from Station
    start = 30000
    stop = 30900
    audioProcessed = audio[start : stop]
    audioProcessed.export("3_english.mp3", format='mp3')

    #4- Input from station

    # 5-Generating to
    start = 31750
    stop = 32200
    audioProcessed = audio[start : stop]
    audioProcessed.export("5_english.mp3", format='mp3')

    # 6- Input to station

   # 7- Train name

    # 8- Generating via
    start = 12900
    stop = 13750
    audioProcessed = audio[start : stop]
    audioProcessed.export("8_english.mp3", format='mp3')

  # 9- via stations

    # 10- Generatingwill arrive on platform number
    start = 38250
    stop = 40850
    audioProcessed = audio[start : stop]
    audioProcessed.export("10_english.mp3", format='mp3')

   # 11- platform number




def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    for index,item in df.iterrows():
        # 2-Input train number from excel file
        textToSpeech(item['train_no'],'2_english.mp3')
        #4- Input from station
        textToSpeech(item['from'], '4_english.mp3')
        # 6- to station
        textToSpeech(item['to'],'6_english.mp3')
        # 7- Train name
        textToSpeech(item['train_name'],'7_english.mp3')
        # 9- via stations
        textToSpeech(item['via'],'9_english.mp3')
        # 11- platform number
        textToSpeech(item['platform'],'11_english.mp3')

        audios=[f"{i}_english.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"english_{item['train_no']}_{index+1}.mp3", format='mp3')


if __name__=='__main__':
    print('Generating Skeleton...')
    generateSkeleton()
    print('Now, lets generate announcement...')
    generateAnnouncement('trains.xlsx')
    print('Done!')