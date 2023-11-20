import os
import shutil
mid_dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/mid_vocal'
mids=os.listdir(mid_dir)
mids=[mid for mid in mids if '.mid' in mid]
targetdir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/mid_vocal/'
for mid in mids:
    songname=mid.replace('.mid','')
    vocal_path='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3/'+songname+'/vocals.mp3'
    target=targetdir+songname+'.mp3'
    shutil.copy(vocal_path, target)