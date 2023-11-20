import os

folder_path = '/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/cutmp3'

# 获取文件夹中的文件名
file_names = os.listdir(folder_path)

# 对文件名进行排序
sorted_file_names = sorted(file_names)

# 打印排序后的文件名
combined_mp3_dir={}
combined_mp3_dir['dt']=0
# for i,file_name in enumerate():
i=0
def calculate_dt(filename):
    st=filename.split('_')[-2]
    assert len(st.split(':'))==2
    assert len(st.split('.'))==2
    st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2])}
    st=st['min']*60+st['s']
    # st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2]),'ms':int(st.split('.')[-1]) if len(st.split('.')[-1])==3 else 10*int(st.split('.')[-1])}
    et=filename.split('_')[-1]
    assert len(et.split(':'))==2
    assert len(et.split('.'))==2
    et={'min':int(et.split(':')[0]),'s':int(et.split(':')[1][:2])}
    et=et['min']*60+et['s']
    dt1=et-st
    return dt1
def analyse_combine(j,sorted_file_names,dt,n=0,ombined_mp3_dirs=[sorted_file_names[i]]):
    if et in (sorted_file_names[i+1])
        dt+=calculate_dt(sorted_file_names[i+1])
        n+=1
        ombined_mp3_dirs=ombined_mp3_dirs+[folder_path+'/'+sorted_file_names[i+1]]
        if dt>=15:
            return n
        else:
            analyse_combine(j+1,sorted_file_names,dt,n)
while i < len(sorted_file_names):
    # if combined_mp3_dir['dt']>=15:
    #     save(combined_mp3_dir)
    # else:
    
    filepath=folder_path+'/'+sorted_file_names[i]
    st=sorted_file_names[i].split('_')[-2]
    assert len(st.split(':'))==2
    assert len(st.split('.'))==2
    st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2])}
    st=st['min']*60+st['s']
    # st={'min':int(st.split(':')[0]),'s':int(st.split(':')[1][:2]),'ms':int(st.split('.')[-1]) if len(st.split('.')[-1])==3 else 10*int(st.split('.')[-1])}
    et=sorted_file_names[i].split('_')[-1]
    assert len(et.split(':'))==2
    assert len(et.split('.'))==2
    et={'min':int(et.split(':')[0]),'s':int(et.split(':')[1][:2])}
    et=et['min']*60+et['s']
    dt=et-st
    # et={'min':int(et.split(':')[0]),'s':int(et.split(':')[1][:2]),'ms':int(et.split('.')[-1]) if len(et.split('.')[-1])==3 else 10*int(et.split('.')[-1])}
    if dt<15:
        if et in (sorted_file_names[i+1]):
            n=analyse_combine(i,sorted_file_names,dt)
            save_combined_mp3(ombined_mp3_dir)
            i+=n
        else:
            i+=1
    else:#>=15s
        # if combined_mp3_dir==[]:#单个文件
        #     copy
        # else:#
        save_combined_mp3(ombined_mp3_dir)
        i+=1
    print(file_name)
