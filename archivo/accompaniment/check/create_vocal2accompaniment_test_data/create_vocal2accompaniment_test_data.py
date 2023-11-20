import os
import shutil
import torchaudio
lrc_dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/val_cutlrc'
lrc_ddir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/check/vocal2accompaniment/lrc'
wav_dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav'
wav_ddir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/check/vocal2accompaniment/wav'
lrc_files=os.listdir(lrc_dir)
i=0
for lrc_file in lrc_files:
    
    songname=lrc_file.replace('.txt','')
    if os.path.exists(wav_dir+'/'+songname+'/'+'vocals.wav'):
        wav,sr=torchaudio.load(wav_dir+'/'+songname+'/'+'vocals.wav')
        if wav.shape[-1]/sr>15:
            i+=1
            lrc_spath=lrc_dir+'/'+lrc_file
            lrc_dpath=lrc_ddir+'/'+lrc_file
            if not os.path.exists(lrc_dpath):
                shutil.copy(lrc_spath, lrc_dpath)
            
            wav_spath=wav_dir+'/'+songname
            wav_dpath=wav_ddir+'/'+songname
            if not os.path.exists(wav_dpath):
                shutil.copytree(wav_spath, wav_dpath)
            if i==5:
                break  
        
