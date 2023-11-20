import torchaudio
import os
import subprocess
def ffmpeg_WavToMP3(input_path, output_path):
    cmd = "ffmpeg -y -i " + input_path + " " + output_path  #将input_path转为.mp3文件
    subprocess.call(cmd, shell=True)
def regenarate_else_remove(wavpath,mp3path):
    ffmpeg_WavToMP3(wavpath, mp3path)
    try: 
        wav,sr=torchaudio.load(mp3path)
    except Exception as e:
        print("An error occurred:", e)
        os.remove(mp3path)
        print("remove:", mp3path)
def regenarate_error_mp3_cutsong(va_wavdir,mp3dir):
    files=os.listdir(mp3dir)
    for i,file in enumerate(files):
        va_path=mp3dir+'/'+file
        try: 
            wav,sr=torchaudio.load(va_path)
        except Exception as e:
            wav_vapath=va_wavdir+'/'+file.replace('.mp3','.wav')
            regenarate_else_remove(wav_vapath,va_path)
va_mp3dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/song_cutmp3_24000hz'
va_wavdir= '/data/huangrm/audioLM/raw_data/cutwav'
regenarate_error_mp3_cutsong(va_wavdir,va_mp3dir)
print('va check over')


def regenarate_error_mp3_a(va_wavdir,mp3dir):
    files=os.listdir(mp3dir)
    for i,file in enumerate(files):
        va_path=mp3dir+'/'+file+'/accompaniment.mp3'
        try: 
            wav,sr=torchaudio.load(va_path)
        except Exception as e:
            wav_vapath=va_wavdir+'/'+file+'/accompaniment.wav'
            regenarate_else_remove(wav_vapath,va_path)
def regenarate_error_mp3_v(va_wavdir,mp3dir):
    files=os.listdir(mp3dir)
    for i,file in enumerate(files):
        va_path=mp3dir+'/'+file+'/vocals.mp3'
        try: 
            wav,sr=torchaudio.load(va_path)
        except Exception as e:
            wav_vapath=va_wavdir+'/'+file+'/vocals.wav'
            regenarate_else_remove(wav_vapath,va_path)
mp3dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3'
wavdir= '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav'
regenarate_error_mp3_a(wavdir,mp3dir)
print('a check over')
regenarate_error_mp3_v(wavdir,mp3dir)
print('v check over')
