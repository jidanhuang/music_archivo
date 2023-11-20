import os
# import torch
# cuda_device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
# torch.cuda.set_device(cuda_device)

datapath='/data/huangrm/audioLM/raw_data/cutwav'
t_path='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav'
wavfiles=os.listdir(datapath)
for wavfile in wavfiles:
    abpath=os.path.join(datapath,wavfile)
    if not os.path.exists(f'{t_path}/'+wavfile.replace('.wav','')):
        os.system(f'spleeter separate -o {t_path} -p spleeter:2stems -B auto {abpath}')
        
        
