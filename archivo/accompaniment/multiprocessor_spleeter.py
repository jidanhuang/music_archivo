import os
import concurrent.futures
import torchaudio
import os
import time
import subprocess
import os

def delete_all_wav_files(folder_path):
    try:
        # 获取文件夹中的所有文件
        file_list = os.listdir(folder_path)
        
        # 遍历文件夹中的文件
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            
            # 检查文件是否是wav格式
            if file_name.endswith('.wav') and os.path.isfile(file_path):
                # 删除文件
                os.remove(file_path)
                print(f"已删除文件: {file_path}")
                
        print("全部wav文件已删除")
    except Exception as e:
        print(f"发生错误: {e}")


#1. ffmpg
def ffmpeg_MP3ToWav(input_path, output_path):
    # 提取input_path路径下所有文件名
    filename = os.listdir(input_path)
    for file in filename:
        path1 = input_path + "/" + file
        path2 = output_path + "/" + os.path.splitext(file)[0]
        cmd = "ffmpeg -i " + path1 + " " + path2 + ".mp3" #将input_path路径下所有音频文件转为.mp3文件
        subprocess.call(cmd, shell=True)

# datapath='/data/huangrm/audioLM/raw_data/cutwav_english'
datapath='/data/huangrm/audioLM/raw_data/cutwav'
wavfiles=os.listdir(datapath)
wavfiles.sort()
# target_path = '/data/huangrm/audioLM/musicgecondn_trainer/archivo/accompaniment/test'
target_path='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3_5stems'
if not os.path.exists(target_path):
    os.mkdir(target_path)
def separate(wavfile):
    abpath = os.path.join(datapath,wavfile)
    save_path = os.path.join(target_path, wavfile.replace('.wav',''))
    if not os.path.exists(save_path):
        os.system(f'spleeter separate -o {target_path} -p spleeter:5stems -B auto {abpath}')
        print(f'spleeter separate -o {target_path} -p spleeter:5stems -B auto {abpath}')
    ffmpeg_MP3ToWav(save_path, save_path)
    delete_all_wav_files(save_path)
    
    
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(separate, wavfile) for wavfile in wavfiles]
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
