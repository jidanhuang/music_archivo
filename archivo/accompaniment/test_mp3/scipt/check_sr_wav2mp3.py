import os
import torchaudio
#check wav
## cutsong/cutva
def check_cutva():
    wav_songdir= '/data/huangrm/audioLM/raw_data/cutwav'
    wav_song=os.listdir(wav_songdir)
    for wav in wav_song:
        wav_songpath=wav_songdir+'/'+wav
        wav,sr=torchaudio.load(wav_songpath)
        print(sr)#24000
check_cutva()
