import os
import shutil

def move_files(source_dir, dest_dir):
    # 遍历文件夹A中的所有文件
    for file_name in os.listdir(source_dir):
        # 构建源文件路径和目标文件路径
        source_file = os.path.join(source_dir, file_name)
        dest_file = os.path.join(dest_dir, file_name)
        # 移动文件
        shutil.move(source_file, dest_file)

# 调用函数进行操作
source_dir = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/train_cutlrc_piano_1'
dest_dir = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/train_cutlrc_piano'

move_files(source_dir, dest_dir)
