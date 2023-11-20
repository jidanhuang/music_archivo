import os
import time
import subprocess
import concurrent.futures
def ffmpeg_MP3ToWav(input_path, output_path):
    # 提取input_path路径下所有文件名
    filename = os.listdir(input_path)
    for file in filename:
        path1 = input_path + "/" + file
        path2 = output_path + "/" + os.path.splitext(file)[0]
        cmd = "ffmpeg -i " + path1 + " " + path2 + ".mp3" #将input_path路径下所有音频文件转为.mp3文件
        subprocess.call(cmd, shell=True)


# #1. ffmpg 单线程
# start_time = time.time()
# wavdir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test'
# mp3dir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3_from_test_ffmpeg'
# songname=os.listdir(wavdir)
# for song in songname:
#     if not os.path.exists(mp3dir+'/'+song):
#         os.mkdir(mp3dir+'/'+song)
#     input_path = wavdir+'/'+song
#     output_path =mp3dir+'/'+song
#     ffmpeg_MP3ToWav(input_path, output_path)
# end_time = time.time()
# execution_time1 = end_time - start_time


# start_time = time.time()
#1. ffmpg 多线程
# wavdir = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test'
# mp3dir = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3_from_test_ffmpeg_mt'


#速度预估：213M/min,预计3-4h转换完
wavdir = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav'
mp3dir = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3'

songname = os.listdir(wavdir)

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    for song in songname:
        if not os.path.exists(mp3dir+'/'+song):
            os.mkdir(mp3dir+'/'+song)

        input_path = wavdir + '/' + song
        output_path = mp3dir + '/' + song

        executor.submit(ffmpeg_MP3ToWav, input_path, output_path)
# end_time = time.time()
# execution_time2 = end_time - start_time
# print('单线程')
# print(execution_time1)
# print(' --------------\n4线程')
# print(execution_time2)

