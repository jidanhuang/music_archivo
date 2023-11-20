import os
from pydub import AudioSegment
import soundfile as sf
import numpy as np
import torch
import torchaudio

def concatenate_audio_files2(file_paths, output_path):
    combined_waveform = None
    sample_rate = None
    
    for file_path in file_paths:
        waveform, current_sample_rate = torchaudio.load(file_path)
        
        if combined_waveform is None:
            combined_waveform = waveform
            sample_rate = current_sample_rate
        else:
            combined_waveform = torch.cat((combined_waveform, waveform), dim=1)
    
    torchaudio.save(output_path, combined_waveform, sample_rate)


def concatenate_audio_files1(file_paths, output_path):
    combined_audio = None
    
    for file_path in file_paths:
        audio, sample_rate = sf.read(file_path)
        
        if combined_audio is None:
            combined_audio = audio
        else:
            combined_audio = np.concatenate((combined_audio, audio))
    
    sf.write(output_path, combined_audio, sample_rate)


def concatenate_audio_files(file_paths, output_path):
    # 创建一个空的音频段，用于存储连接后的音频
    combined_audio = AudioSegment.silent(duration=0)
    
    # 遍历输入的音频文件路径列表
    for file_path in file_paths:
        audio = AudioSegment.from_file(file_path)
        combined_audio += audio
    
    # 保存连接后的音频为新文件
    combined_audio.export(output_path.replace('.wav','.mp3'), format="mp3")
    print(output_path)
# # 示例文件路径列表和输出路径
# input_files = ["file1.wav", "file2.wav", "file3.wav"]
# output_file = "combined_output.wav"

# # 调用函数进行连接并保存
# concatenate_audio_files(input_files, output_file)

folder_path = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav'
# folder_path = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav'
combined_dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3_combined'
# 获取文件夹中的文件名
file_names = os.listdir(folder_path)

# 对文件名进行排序
sorted_file_names = sorted(file_names)
def remove_overlap_from_list(main_list, sublist):
    for item in sublist:
        main_list.remove(item)
    return main_list
songnames=[]

def combine_and_save(songcuts,songname):
    if not os.path.exists(combined_dir+'/'+songname):
        os.mkdir(combined_dir+'/'+songname)
    vocal_dir=[folder_path+'/'+songcut+'/vocals.wav' for songcut in songcuts]  
    a_dir=[folder_path+'/'+songcut+'/accompaniment.wav' for songcut in songcuts]  
    t_vocal_dir=combined_dir+'/'+songname+'/vocals.wav'
    t_a_dir=combined_dir+'/'+songname+'/accompaniment.wav' 
    concatenate_audio_files(sorted(vocal_dir), t_vocal_dir)
    concatenate_audio_files(sorted(a_dir), t_a_dir)
def check(songcuts):
    for i,songcut in enumerate(songcuts):
        et=songcut.split('_')[-1]
        assert len(et.split(':'))==2
        # assert len(et.split('.'))==2
        if i==len(songcuts)-1 or et in songcuts[i+1]  :
            pass
        else: return False
    return True
def get_cuts(songname,sorted_file_names,songcuts=[]):
    l=len(songname)
    for file in sorted_file_names:
        if file[:l+1]==songname+'_':
            songcuts.append(file)
    sorted_file_names=remove_overlap_from_list(sorted_file_names, songcuts)
    return songcuts,sorted_file_names
for i,filename in enumerate(sorted_file_names):
    st=filename.split('_')[-2]
    assert len(st.split(':'))==2
    # assert len(st.split('.'))==2
    # st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2])}
    # st=st['min']*60+st['s']
    # st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2]),'ms':int(st.split('.')[-1]) if len(st.split('.')[-1])==3 else 10*int(st.split('.')[-1])}
    et=filename.split('_')[-1]
    assert len(et.split(':'))==2
    # assert len(et.split('.'))==2
    # et={'min':int(et.split(':')[0]),'s':int(et.split(':')[1][:2])}
    # et=et['min']*60+et['s']
    songnames.append(filename.replace(f'_{st}_{et}',''))
songnames=sorted(list(set(songnames)))
for songname in songnames: 
    songcuts,sorted_file_names=get_cuts(songname,sorted_file_names,songcuts=[])
    if check(songcuts):
        # continue
        try:
            combine_and_save(songcuts,songname)
        except:
            print(songname+' fail\n ------------------------')

        # combine_and_save(songcuts,songname)


















# 打印排序后的文件名
combined_wav_dir={}
combined_wav_dir['dt']=0
# for i,file_name in enumerate():
i=0
def calculate_dt(filename):
    st=filename.split('_')[-2]
    assert len(st.split(':'))==2
    assert len(st.split('.'))==2
    st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2])}
    st=st['min']*60+st['s']
    # st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2]),'ms':int(st.split('.')[-1]) if len(st.split('.')[-1])==3 else 10*int(st.split('.')[-1])}
    et=filename.split('_')[-1]
    assert len(et.split(':'))==2
    assert len(et.split('.'))==2
    et={'min':int(et.split(':')[0]),'s':int(et.split(':')[1][:2])}
    et=et['min']*60+et['s']
    dt1=et-st
    return dt1
while i < len(sorted_file_names):
    # if combined_wav_dir['dt']>=15:
    #     save(combined_wav_dir)
    # else:
    
    filepath=folder_path+'/'+sorted_file_names[i]
    st=sorted_file_names[i].split('_')[-2]
    assert len(st.split(':'))==2
    assert len(st.split('.'))==2
    st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2])}
    st=st['min']*60+st['s']
    # st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2]),'ms':int(st.split('.')[-1]) if len(st.split('.')[-1])==3 else 10*int(st.split('.')[-1])}
    et=sorted_file_names[i].split('_')[-1]
    assert len(et.split(':'))==2
    assert len(et.split('.'))==2
    et={'min':int(et.split(':')[0]),'s':int(et.split(':')[1][:2])}
    et=et['min']*60+et['s']
    dt=et-st

