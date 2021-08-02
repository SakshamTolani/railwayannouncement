import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    myText=str(text)
    language="hi"
    myObj=gTTS(text=myText,lang=language, slow=False)
    myObj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio=AudioSegment.from_mp3('announcement.mp3')
    # 1-Generating Yatrigan kripya dhyaan dijiye gaadi number
    start = 41200
    stop = 48200
    audioProcessed = audio[start : stop]
    audioProcessed.export("1_hindi.mp3", format='mp3')

    # 2-Input train number from excel file

    # 3-Input from Station

    # 4-Generating se chalkar
    start = 9200
    stop = 9900
    audioProcessed = audio[start : stop]
    audioProcessed.export("3_hindi.mp3", format='mp3')

    # 5- to station

    # 6- Train name

    #7- Generating via
    start = 12900
    stop = 13750
    audioProcessed = audio[start : stop]
    audioProcessed.export("6_hindi.mp3", format='mp3')

    # 8- via stations

    # 9- Generating thodi der mein platform number
    start = 15800
    stop = 18250
    audioProcessed = audio[start : stop]
    audioProcessed.export("8_hindi.mp3", format='mp3')

    # 10- platform number

    # 11- Generating par aa rhi hai

    start = 62900
    stop = 64500
    audioProcessed = audio[start : stop]
    audioProcessed.export("10_hindi.mp3", format='mp3')


def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    for index,item in df.iterrows():
        # 2-Input train number from excel file
        textToSpeech(item['train_no']+ " "+" " + item['from'],'2_hindi.mp3')
        # 5- to station
        textToSpeech(item['to'],'4_hindi.mp3')
        # 6- Train name
        textToSpeech(item['train_name'],'5_hindi.mp3')
        # 8- via stations
        textToSpeech(item['via'],'7_hindi.mp3')
        # 10- platform number
        textToSpeech(item['platform'],'9_hindi.mp3')

        audios=[f"{i}_hindi.mp3" for i in range(1,11)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format='mp3')


if __name__=='__main__':
    print('Generating Skeleton...')
    generateSkeleton()
    print('Now, lets generate announcement...')
    generateAnnouncement('trains.xlsx')
    print('Done!')