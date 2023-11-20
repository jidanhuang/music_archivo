import os
import torchaudio
import subprocess

def check_accompaniment(mp3dir):
    for i,file in enumerate(os.listdir(mp3dir)):
        accompaniment_path=mp3dir+'/'+file+'/accompaniment.mp3'
        try: 
            wav,sr=torchaudio.load(accompaniment_path)
        except Exception as e:
            print(i)
            print(f'{accompaniment_path} ')
            print("An error occurred:", e)
        duration=wav.shape[-1]/sr
        if duration<0.5:
            print(f'{accompaniment_path} <0.5s')
def check_vocals(mp3dir):
    for i,file in enumerate(os.listdir(mp3dir)):
        vocals_path=mp3dir+'/'+file+'/vocals.mp3'
        try: 
            wav,sr=torchaudio.load(vocals_path)
        except Exception as e:
            print(i)
            print(f'{vocals_path} ')
            print("An error occurred:", e)
        duration=wav.shape[-1]/sr
        if duration<0.5:
            print(f'{vocals_path} <0.5s')
def check_va(mp3dir):
    files=os.listdir(mp3dir)
    for i,file in enumerate(files):
        va_path=mp3dir+'/'+file
        try: 
            wav,sr=torchaudio.load(va_path)
        except Exception as e:
            print(i)
            print(f'{va_path} ')
            print("An error occurred:", e)
        duration=wav.shape[-1]/sr
        if duration<0.5:
            print(f'{va_path} <0.5s')
vadir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/song_cutmp3_24000hz'
check_va(vadir)
print('va check over')

vadir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3'
check_accompaniment(vadir)
print('a check over')

check_vocals(vadir)
print('v check over')