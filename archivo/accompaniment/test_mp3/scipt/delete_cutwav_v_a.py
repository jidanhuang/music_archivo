import os
import torchaudio
mp3dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3'
wavdir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav'
for file in os.listdir(mp3dir):
    vpath=mp3dir+'/'+file+'/vocals.mp3'    
    apath=mp3dir+'/'+file+'/accompaniment.mp3'
    v_wavpath=wavdir+'/'+file+'/vocals.wav'    
    a_wavpath=wavdir+'/'+file+'/accompaniment.wav'
    #v
    try :
        wav,sr=torchaudio.load(vpath)
        duration=wav.shape[-1]/sr
        if duration>0.2:
            os.remove(v_wavpath)
    except Exception  as e:
        print('an error occurs:',e)
        print(vpath)
        print('----------------')    
    #a    
    try :
        wav,sr=torchaudio.load(apath)
        duration=wav.shape[-1]/sr
        if duration>0.2:
            os.remove(a_wavpath)
    except Exception  as e:
        print('an error occurs:',e)
        print(apath)
        print('----------------')