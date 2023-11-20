import os 
import argparse
import numpy as np
def mid2wav(wavdir,middir,meldir):
    # fname=np.load('fname.npy')
    # fname=fname.tolist()
    # mels=os.listdir(meldir)
    filenames=[]
    mids=os.listdir(middir)
    # for mel in mels:
    #     filenames.append(mel.replace(".npy","")[:-18])
    for file in mids:
        # if file.replace(".mid","") not in filenames:
            # file=filename+".mid"
        if '.mid' in file:
            abpath=os.path.join(middir,file)
            if(not os.path.exists(os.path.join(wavdir,file.replace(".mid",".wav"))) and os.path.exists(abpath) and not os.path.exists(os.path.join(middir,file.replace(".mid",".wav")))):
                os.system("java -jar archivo/accompaniment/midi2wav.jar {}".format(abpath))
                print("java -jar archivo/accompaniment/midi2wav.jar {}".format(abpath))
    # for root,dirs,files in os.walk(middir):
    #     for file in files:
    #         abpath=os.path.join(root,file)
    #         if(not os.path.exists(os.path.join(wavdir,file.replace(".mid",".wav")))):
    #             os.system("java -jar midi2wav.jar {}".format(abpath))
    #             print("java -jar midi2wav.jar {}".format(abpath))
def movewav(wavdir,middir):
    for root,dirs,files in os.walk(middir):
        for file in files:
            if ".wav" in file:
                abpath=os.path.join(root,file)
                if not os.path.exists(wavdir):
                    os.mkdir(wavdir)
                wavpath=os.path.join(wavdir,file)
                os.rename(abpath,wavpath)
def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--wavdir', default="/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/pianowav",type=str)
    parser.add_argument('--middir', default="/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/mid",type=str)
    parser.add_argument('--meldir', default="data/processed_1117/mel",type=str)

    args = parser.parse_args()
    mid2wav(args.wavdir,args.middir,args.meldir)
    movewav(args.wavdir,args.middir)
if __name__ =='__main__':
    main()
