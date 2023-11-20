from pydub import AudioSegment
import torchaudio
import os
def convert_wav_to_flac(wav_path, flac_path):
    # 加载WAV文件
    audio = AudioSegment.from_wav(wav_path)
    # 导出为flac文件（采样率不变）
    audio.export(flac_path, format='flac')
def check_sr(audiopath):
    wav,sr=torchaudio.load(audiopath)
    print(audiopath)
    print(sr)
    print(wav.shape[-1]/sr)
    print('------------------------')
# 示例用法
# wav_path = '输入文件.wav'
#把分离wav转换成flac
# flac_path = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_flac/flac_pydub/一剪梅-费玉清.flac'
# convert_wav_to_flac(audiopath, flac_path)

wavdir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test'
flacdir='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/flac_from_test_pydub'
songname=os.listdir(wavdir)
for song in songname:
    if not os.path.exists(flacdir+'/'+song):
        os.mkdir(flacdir+'/'+song)
    vocal_path=wavdir+'/'+song+'/vocals.wav'    
    accompaniment_path=wavdir+'/'+song+'/accompaniment.wav'
    vocal_path_flac=flacdir+'/'+song+'/vocals.flac'    
    accompaniment_path_flac=flacdir+'/'+song+'/accompaniment.flac'
    convert_wav_to_flac(vocal_path, vocal_path_flac)
    convert_wav_to_flac(accompaniment_path, accompaniment_path_flac)
    check_sr(vocal_path)
    check_sr(vocal_path_flac)
    check_sr(accompaniment_path)
    check_sr(accompaniment_path_flac)
    
# 比例mp3:flac:wav=1:4:10