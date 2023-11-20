import torchaudio
import os
datadir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3_5stems'
mp3files=os.listdir(datadir)
for mp3file in mp3files:
    filedir=datadir+'/'+mp3file
    wav_shape=[]
    for mp3 in os.listdir(filedir):
        mp3path=filedir+'/'+mp3
        wav,sr=torchaudio.load(mp3path)
        wav_shape.append(wav.shape)
    assert all(x == wav_shape[0] for x in wav_shape)
        