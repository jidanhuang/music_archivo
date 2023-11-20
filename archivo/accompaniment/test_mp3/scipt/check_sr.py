import torchaudio
#下载的musicB mp3 44100
#分离出的wav是 44100
#分离出的wav用AudioSegment转换成MP3还是44100

#分离出的乐器
# audiopath='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/16hz/一剪梅-费玉清/bass.wav'
# wav,sr=torchaudio.load(audiopath)
# print(audiopath)
# print(sr)
# print(wav.shape[-1]/sr)
# spleeter separate -o /data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3 -p spleeter:5stems -B auto /data/huangrm/audioLM/MusicB0/一剪梅-费玉清.mp3

audiopath='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3/一剪梅-费玉清/bass.wav'
wav,sr=torchaudio.load(audiopath)
print(audiopath)
print(sr)
print(wav.shape[-1]/sr)

#下载的MP3
mp3_path='/data/huangrm/audioLM/MusicB0/一剪梅-费玉清.mp3'
# /data/huangrm/audioLM/raw_data/MusicB
wav,sr=torchaudio.load(mp3_path)
print(mp3_path)
print(sr)
print(wav.shape[-1]/sr)

from pydub import AudioSegment

def convert_wav_to_mp3(wav_path, mp3_path):
    # 加载WAV文件
    audio = AudioSegment.from_wav(wav_path)

    # 导出为MP3文件（采样率不变）
    audio.export(mp3_path, format='mp3')

# 示例用法
# wav_path = '输入文件.wav'
#把分离wav转换成mp3
mp3_path = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3_pydub/一剪梅-费玉清.mp3'
convert_wav_to_mp3(audiopath, mp3_path)



wav,sr=torchaudio.load(mp3_path)
print(mp3_path)
print(sr)
print(wav.shape[-1]/sr)




import subprocess
def convert_wav_to_mp3(wav_path, mp3_path):
    # 调用FFmpeg进行音频转换
    command = f'ffmpeg -i {wav_path} -ar $(ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate -of default=nw=1:nk=1) {mp3_path}'
    subprocess.call(command, shell=True)

# 示例用法
mp3_path='/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/mp3_ffmpg/一剪梅-费玉清.mp3'
convert_wav_to_mp3(audiopath, mp3_path)


wav,sr=torchaudio.load(mp3_path)
print(mp3_path)
print(sr)
print(wav.shape[-1]/sr)


# 