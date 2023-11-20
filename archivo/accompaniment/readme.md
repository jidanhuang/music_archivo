## 1.convert wav to accompaniments
 pip install spleeter==2.3.2 ffmpeg ffmpeg-python  -i https://mirrors.aliyun.com/pypi/simple/
    nohup python -u archivo/accompaniment/multiprocessor_spleeter.py > archivo/accompaniment/multiprocessor_spleeter.log 2>&1 &
    nohup python -u archivo/accompaniment/spleeter.py > archivo/accompaniment/spleeter.log 2>&1 &
## 根据wav文件夹的文件生成歌词文件
    1)根据wav复制对应lrc文件：（不用修改source_folder为wav文件夹，修改确定val/train）。并
    python archivo/accompaniment/cutlrc.py
    2）加入keyword和wangyi prompt
    python archivo/keyword/ifidf_keybert.py
    2)lrc加入prompt：修改相关路径并
    python archivo/accompaniment/add_prompt.py
    nohup python -u archivo/accompaniment/add_prompt.py > archivo/accompaniment/add_prompt.log 2>&1 &
    val_lrc不增加，目前只少量，只增加train_lrc
## 2.convert accompaniments into midi
    using transcript_wav_to_midi.py,
    default_output_dir:mid
    command:
        nohup python -u archivo/accompaniment/transcript_wav_to_midi.py --audio_path /data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav --output_midi_path /data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/mid --cuda --checkpoint_path /data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/ckpts/CRNN_note_F1=0.9677_pedal_F1=0.9186.pth --dir_mode > archivo/accompaniment/transcript_wav_to_midi.log 2>&1 & 
#  注：vocal to midi
    using transcript_vocalmp3_to_midi.py,
    default_output_dir:mid_vocal
    command:
        nohup python -u archivo/accompaniment/transcript_vocalmp3_to_midi.py --audio_path /data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3 --output_midi_path /data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/mid_vocal --cuda --checkpoint_path /data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/ckpts/CRNN_note_F1=0.9677_pedal_F1=0.9186.pth --dir_mode > archivo/accompaniment/transcript_vocalmp3_to_midi.log 2>&1 & 
## 3.convert midi to wav:using virtualMIDISynth
    nohup python -u archivo/accompaniment/midi_to_wav.py > archivo/accompaniment/midi_to_wav.log 2>&1 &
