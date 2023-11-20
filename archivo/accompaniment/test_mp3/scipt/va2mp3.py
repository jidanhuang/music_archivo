from pydub import AudioSegment
import torchaudio
import os
import time
import subprocess
start_time = time.time()
#1. ffmpg
def ffmpeg_MP3ToWav(input_path, output_path):
    # 提取input_path路径下所有文件名
    filename = os.listdir(input_path)
    for file in filename:
        path1 = input_path + "/" + file
        path2 = output_path + "/" + os.path.splitext(file)[0]
        cmd = "ffmpeg -i " + path1 + " " + path2 + ".mp3" #将input_path路径下所有音频文件转为.mp3文件
        subprocess.call(cmd, shell=True)
def check_sr(audiopath):
    wav,sr=torchaudio.load(audiopath)
    print(audiopath)
    print(sr)
    print(wav.shape[-1]/sr)
    print('------------------------')

wavdir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test'
mp3dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3_from_test_ffmpeg'
songname=os.listdir(wavdir)
for song in songname:
    if not os.path.exists(mp3dir+'/'+song):
        os.mkdir(mp3dir+'/'+song)
    input_path = wavdir+'/'+song
    output_path =mp3dir+'/'+song
    ffmpeg_MP3ToWav(input_path, output_path)
    vocal_path=wavdir+'/'+song+'/vocals.wav'    
    accompaniment_path=wavdir+'/'+song+'/accompaniment.wav'
    vocal_path_mp3=mp3dir+'/'+song+'/vocals.mp3'    
    accompaniment_path_mp3=mp3dir+'/'+song+'/accompaniment.mp3'
    check_sr(vocal_path)
    check_sr(vocal_path_mp3)
    check_sr(accompaniment_path)
    check_sr(accompaniment_path_mp3)
    
end_time = time.time()
execution_time1 = end_time - start_time





start_time = time.time()
#2. pydub
def convert_wav_to_mp3(wav_path, mp3_path):
    # 加载WAV文件
    audio = AudioSegment.from_wav(wav_path)
    # 导出为MP3文件（采样率不变）
    audio.export(mp3_path, format='mp3')
def check_sr(audiopath):
    wav,sr=torchaudio.load(audiopath)
    print(audiopath)
    print(sr)
    print(wav.shape[-1]/sr)
    print('------------------------')
# 示例用法
# wav_path = '输入文件.wav'
#把分离wav转换成mp3
# mp3_path = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3_pydub/一剪梅-费玉清.mp3'
# convert_wav_to_mp3(audiopath, mp3_path)

wavdir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test'
mp3dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3_from_test_pydub'
songname=os.listdir(wavdir)
for song in songname:
    if not os.path.exists(mp3dir+'/'+song):
        os.mkdir(mp3dir+'/'+song)
    vocal_path=wavdir+'/'+song+'/vocals.wav'    
    accompaniment_path=wavdir+'/'+song+'/accompaniment.wav'
    vocal_path_mp3=mp3dir+'/'+song+'/vocals.mp3'    
    accompaniment_path_mp3=mp3dir+'/'+song+'/accompaniment.mp3'
    convert_wav_to_mp3(vocal_path, vocal_path_mp3)
    convert_wav_to_mp3(accompaniment_path, accompaniment_path_mp3)
    check_sr(vocal_path)
    check_sr(vocal_path_mp3)
    check_sr(accompaniment_path)
    check_sr(accompaniment_path_mp3)
end_time = time.time()
execution_time2 = end_time - start_time
print('ffmpeg')
print(execution_time1)#更快
print('----------------')
print('pydub')
print(execution_time2)


