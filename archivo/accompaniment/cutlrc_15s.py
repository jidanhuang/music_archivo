import os
import re
import numpy as np
import random
cutwavpath="/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3_15s"
train_cutlrcpath="/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/train_cutlrc_15s"
val_cutlrcpath="/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/val_cutlrc_15s"
datapath="/data/huangrm/audioLM/raw_data/MusicB"
if not os.path.exists(train_cutlrcpath):
    os.makedirs(train_cutlrcpath)
if not os.path.exists(val_cutlrcpath):
    os.makedirs(val_cutlrcpath)
def setup_seed(seed):
   np.random.seed(seed)
   random.seed(seed)
# 设置随机数种子
def timedayu(t1,t2):
    a=int (t1[:2])
    b=int(t1[3:5])
    c=int(t1[6:])
    if int (t1[:2])>int (t2[:2]):
        return True
    elif int (t1[:2])==int (t2[:2]) and int(t1[3:5])>int(t2[3:5]):
        return True
    elif int (t1[:2])==int (t2[:2]) and int(t1[3:5])==int(t2[3:5]) and int(t1[6:])>=int(t2[6:]):
        return True
    else:
        return False
def matchlrc(datatype):
    cutmp3=os.listdir(cutwavpath)
    random.shuffle(cutmp3)
    if datatype=='val':
        cutmp3=cutmp3[:180]
        cutlrcpath=val_cutlrcpath
    elif datatype=='train':
        cutmp3=cutmp3[180:]
        cutlrcpath=train_cutlrcpath
    for file in cutmp3:
        #wav文件起始时间
        lrcpath_tosave=os.path.join(cutlrcpath,file+'.txt')
        abpath=os.path.join(cutwavpath,file)
        file_splitlist = file.split("_")
        id_15s=file_splitlist[-1]
        filename=file.replace('_'+id_15s,'')
        print(file,":")
        id_15s=int(id_15s)
        start_s=15*id_15s-15
        end_s=15*id_15s
        
        start=[int(np.floor(start_s/60)),start_s%60]
        start_1 = ''.join([ ":", f'{start[1]:02d}', ".", '00'])
        start=f'{start[0]:02d}{start_1}'
        
        end =[int(np.floor(end_s/60)),end_s%60]
        end_1 = ''.join([ ":", f'{end[1]:02d}', ".", '00'])
        end=f'{end[0]:02d}{end_1}'
        lrcpath = os.path.join(datapath, ''.join([filename, ".lrc"]))
        if not os.path.exists(lrcpath):
            # os.remove(abpath)
            print(abpath,'has no lrc file')
            continue
        with open(lrcpath,"r") as f:
            lrc = f.read()
            f.close()
        lrclst = lrc.splitlines()
        # print("lrclst",lrclst)
        newlrclst=[]
        for line in lrclst:#有时间戳，且不是说明
            if ("]"  in line) and ("未经许可" not in line) and  ("：" not in line.split("]")[-1]) and  (":" not in line.split("]")[-1]):
                newlrclst.append(line)

        #时间列表timelst
        timelst = []
        if   newlrclst==[]:#防止无时间戳
            print(abpath,"has no timestamp","newlrclst=",newlrclst)
            continue
        if newlrclst[0].count(":")==2:#防止12:30:20格式
            print(abpath,"has two ':' ")
            continue
        for index, line in enumerate(newlrclst):
            time = line.split("]")[0].split("[")[-1]   
            if "." not in time:
                time="".join([time,".00"])
            millisec=time.split(":")[-1].split(".")[-1]
            if len(millisec)==3:
                time=time[:-1]
            timelst.append(time)
            newlrclst[index] = line.split("]")[-1]
        er=0#如果时间戳长度有误
        for time in timelst:
            if len(time)!=8:
                print(time,"is too long")
                er=1
        if er==1:
            
            continue
        # print("timelst",timelst)
        # print("newlrclst",newlrclst)
        #生成歌词
        for i, t in enumerate(timelst):
            if i == len(timelst) - 1:
                endi = i
                if (timedayu(start, t)):
                    starti=i
                break
            # print(t, start, timelst[i + 1])
            if (timedayu(start, t) and timedayu(timelst[i + 1], start)) or (i == 0 and timedayu(t, start)):
                starti = i
            if timedayu(end, t) and timedayu(timelst[i + 1], end):
                endi = i + 1
                break
        # print(starti, endi)
        newlrclst = newlrclst[starti:endi + 1]
        # spe=0
        for i in range(len(newlrclst)):#去除每行歌词的空格“\xa0”和含有特殊字符的句子
            mc=u'[’·°!"#$%&\'()*+,-./:;<=>?@，。?★、…【】*→←〖〗（）《》？“”‘’！[\\]^_`{|}~｛｝]+'
            if re.search(mc,newlrclst[i])!=None or "版权" in newlrclst[i] or "网易" in newlrclst[i] or "未经" in newlrclst[i]:
                print(newlrclst[i])
                newlrclst[i]=""
            if "\xa0" in newlrclst[i]:
                newlrclst[i] = "".join(newlrclst[i].split("\xa0"))
            if "\u3000" in newlrclst[i]:
                newlrclst[i] = "".join(newlrclst[i].split("\u3000"))
            while " " in newlrclst[i]:
                newlrclst[i]=newlrclst[i].replace(" ","")
        # if spe==1:
        #     continue
        txtlst = [x.strip() for x in newlrclst if x.strip()!='']
        lrc = ' '.join(txtlst)
        savepath =lrcpath_tosave
        savepath =savepath.replace(".wav",".txt") # 保存为txt
        if not os.path.exists(savepath):
            with open(savepath, 'w') as f:
                f.write(lrc)
setup_seed(3407)
matchlrc('val')
print('val over')
matchlrc('train')
print('train over')










