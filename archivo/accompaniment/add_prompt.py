import os

# 文件夹路径
folder_path = 'archivo/accompaniment/train_cutlrc'

# 遍历文件夹
for filename in os.listdir(folder_path):
    # 检查文件是否为 txt 文件
    if filename.endswith('.txt'):
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, filename)

        # 打开文件进行读取和写入
        with open(file_path, 'r+') as file:
            # 读取原始内容
            content = file.read()
            if '伴奏：'!=content[:3]:#如果没有加prompt
                # 将文件指针移到文件开头
                file.seek(0, 0)

                # 写入添加前缀后的内容
                file.write('伴奏：' + content)
                print(file)

        # 关闭文件
        file.close()
print('finish')
