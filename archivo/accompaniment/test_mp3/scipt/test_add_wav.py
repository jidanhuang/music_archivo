import os
import torchaudio
import torch
folder_path = "/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/16hz/一剪梅-费玉清"  # 修改为实际的文件夹路径

wav_files = [file for file in os.listdir(folder_path) if file.endswith(".wav")]
waveforms=[]
for wav_file in wav_files:
    wav_path = os.path.join(folder_path, wav_file)
    waveform, sample_rate = torchaudio.load(wav_path)
    waveforms.append(waveform)

# 使用 torch.stack 将 Tensor 列表堆叠起来，得到一个新的维度
stacked_tensors = torch.stack(waveforms)

# 使用 torch.sum 在新维度上逐元素相加
sum_result = torch.sum(stacked_tensors, dim=0)

output_folder = "/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/test_mp3/wav_added"  # 修改为输出文件夹路径

output_path = os.path.join(output_folder, "sum_result.wav")
torchaudio.save(output_path, sum_result, sample_rate=sample_rate)  # 假设 sample_rate 已知

print(f"Saved WAV file to {output_path}")
