import os
import shutil

def copy_filename_txt(source_dir):
    for filename in os.listdir(source_dir):
        # Check if 'cutlrc' folder exists in the current subdirectory
        cutlrc_dir = source_dir.replace('cutwav','val_cutlrc')
        train_cutlrc_dir = source_dir.replace('cutwav','train_cutlrc')
        source_file = os.path.join('/data/huangrm/audioLM/raw_data/cutlrc', f'{filename}.txt')
        if os.path.exists(cutlrc_dir) and os.path.isdir(cutlrc_dir) and os.path.exists(source_file) :#
            if not os.path.exists(os.path.join(cutlrc_dir , f'{filename}.txt')) and not os.path.exists(os.path.join(train_cutlrc_dir , f'{filename}.txt')):
            #如果val和train的歌词文件夹都没有对应文件，就新增
            # 训练集歌词文件
                new_train_cutlrc_dir = source_dir.replace('cutwav','train_cutlrc_new')
                # Copy 'filename.txt' to 'cutlrc' folder
                target_file = os.path.join(new_train_cutlrc_dir, f'{filename}.txt')
                shutil.copyfile(source_file, target_file)
                print(target_file)
# Specify the source directory and target directory
source_folder = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutwav'

copy_filename_txt(source_folder)


def copy_piano_filename_txt(source_dir):
    for filename in os.listdir(source_dir):
        filename=filename.replace('.wav','')
        # Check if 'cutlrc' folder exists in the current subdirectory
        cutlrc_dir = source_dir.replace('pianowav','val_cutlrc_piano')
        train_cutlrc_dir = source_dir.replace('pianowav','train_cutlrc_piano')
        new_train_cutlrc_dir = source_dir.replace('pianowav','train_cutlrc_piano_1')
        source_file = os.path.join('/data/huangrm/audioLM/raw_data/cutlrc', f'{filename}.txt')
        if os.path.exists(cutlrc_dir) and os.path.isdir(train_cutlrc_dir) and os.path.exists(source_file) :
            if not os.path.exists(os.path.join(cutlrc_dir , f'{filename}.txt')) and not os.path.exists(os.path.join(train_cutlrc_dir , f'{filename}.txt')):
            #如果val和train的歌词文件夹都没有对应文件，就新增训练集歌词文件
                # Copy 'filename.txt' to 'cutlrc' folder
                target_file = os.path.join(new_train_cutlrc_dir, f'{filename}.txt')
                shutil.copyfile(source_file, target_file)
                print(source_file)

source_folder = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/pianowav'
# copy_piano_filename_txt(source_folder)
