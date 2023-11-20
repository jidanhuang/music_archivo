## cutmp3_combined-> cutmp3_15s
import os
import torchaudio

def slice_and_save_audio(input_folder, output_folder, slice_duration=15):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for sub_folder_name in os.listdir(input_folder):
        sub_folder_path = os.path.join(input_folder, sub_folder_name)
        
        if os.path.isdir(sub_folder_path):
            vocals_file_path = os.path.join(sub_folder_path, "vocals.mp3")
            accompaniment_file_path = os.path.join(sub_folder_path, "accompaniment.mp3")
            
            if os.path.exists(vocals_file_path) and os.path.exists(accompaniment_file_path):
                vocals_waveform, sample_rate = torchaudio.load(vocals_file_path)
                accompaniment_waveform, _ = torchaudio.load(accompaniment_file_path)
                
                slice_length = sample_rate * slice_duration
                num_slices = vocals_waveform.size(1) // slice_length
                
                for i in range(num_slices):
                    start = i * slice_length
                    end = (i + 1) * slice_length
                    
                    vocals_slice = vocals_waveform[:, start:end]
                    accompaniment_slice = accompaniment_waveform[:, start:end]
                    
                    # 如果切片的长度满足要求（大于等于15秒），则保存
                    if vocals_slice.size(1) >= slice_length:
                        output_sub_folder_name = f"{sub_folder_name}_{i+1}"
                        output_sub_folder_path = os.path.join(output_folder, output_sub_folder_name)
                        os.makedirs(output_sub_folder_path, exist_ok=True)
                        
                        output_vocals_file_path = os.path.join(output_sub_folder_path, "vocals.mp3")
                        output_accompaniment_file_path = os.path.join(output_sub_folder_path, "accompaniment.mp3")
                        if os.path.exists(output_vocals_file_path) and os.path.exists(output_accompaniment_file_path):
                            continue
                        else:
                            torchaudio.save(output_vocals_file_path, vocals_slice, sample_rate)
                            torchaudio.save(output_accompaniment_file_path, accompaniment_slice, sample_rate)
                            print(output_accompaniment_file_path)



# 输入和输出文件夹路径
input_folder = "/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3_combined"
output_folder = "/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3_15s"

# 调用函数进行切片并保存
slice_and_save_audio(input_folder, output_folder)
