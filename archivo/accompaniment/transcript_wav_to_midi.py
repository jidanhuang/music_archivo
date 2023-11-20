import os
import argparse
import torch
import time
from tqdm import tqdm
import numpy as np
from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
import concurrent.futures

def inference(args, transcriptor, audio_path, output_midi_path, print_log=True):
    """Inference template.

    Args:
      model_type: str
      audio_path: str
      cuda: bool
    """

    # Arugments & parameters
    # audio_path = args.audio_path
    # output_midi_path = args.output_midi_path

    # Load audio
    if print_log:
        print(audio_path)
    try:
        (audio, _) = load_audio(audio_path, sr=sample_rate, mono=True)
    except:
        print("fail to load",audio_path)
        return
    """device: 'cuda' | 'cpu'
    checkpoint_path: None for default path, or str for downloaded checkpoint path.
    """

    # Transcribe and write out to MIDI file
    transcribe_time = time.time()
    transcribed_dict = transcriptor.transcribe(audio, output_midi_path)
    if print_log:
        print('Transcribe time: {:.3f} s'.format(time.time() - transcribe_time))

def recordflow(audio_path):
    files=os.listdir(audio_path)
    fname=[]
    for file in files:
        filename=file.replace(".wav","")
        fname.append(filename)
    fname=np.array(fname)
    np.save('/data/huangrm/audioLM/musicgen_trainer/archivo/accompaniment/fname.npy',fname) 
def process_file(args, transcriptor, filename):
    fn = os.path.basename(filename).replace('.wav', '')
    output_midi_path = os.path.join(args.output_midi_path, fn + ".mid")
    if os.path.exists(output_midi_path):
        return
    inference(args, transcriptor, filename, output_midi_path)
def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--audio_path', type=str, required=True)
    parser.add_argument('--output_midi_path', type=str, required=True)
    parser.add_argument('--cuda', action='store_true', default=True)
    parser.add_argument('--checkpoint_path', default=None)
    parser.add_argument('--dir_mode', action='store_true', default=False)

    args = parser.parse_args()#记录这一批的文件名
    recordflow(args.audio_path)
    device = 'cuda' if args.cuda and torch.cuda.is_available() else 'cpu'#cudatoolkit 10.1.243
    print(torch.cuda.is_available())
    # Transcriptor
    transcriptor = PianoTranscription(device=device, checkpoint_path=args.checkpoint_path)
    if not os.path.exists(args.output_midi_path):
        os.mkdir(args.output_midi_path)
    # if args.dir_mode:
    #     filenames = [os.path.join(args.audio_path, f, 'accompaniment.wav') for f in os.listdir(args.audio_path)]
    # else:
    #     filenames = [args.audio_path]
    # filenames = [os.path.join(args.audio_path, f, 'accompaniment.wav') for f in os.listdir(args.audio_path)]
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     executor.map(lambda filename: process_file(args, transcriptor, filename), filenames)    # if args.dir_mode:
    if args.dir_mode:
        for f in tqdm(os.listdir(args.audio_path)):
            # if not f.endswith(".wav"):
            #     continue
            fn = f#os.path.basename(f).replace('.wav','')
            output_midi_path = os.path.join(args.output_midi_path, fn+ ".mid")
            # print(output_midi_path)
            # exit()
            if os.path.exists(output_midi_path):
                continue
            # print('start')
            inference(args, transcriptor, os.path.join(args.audio_path, f,'accompaniment.wav'), output_midi_path)
    else:
        audio_path = args.audio_path
        output_midi_path = args.output_midi_path
        inference(args, transcriptor, os.path.join(args.audio_path, f,'accompaniment.wav'), output_midi_path)

        
if __name__ == '__main__':

    main()
    # wavdir="accomponimentsandvocal"
    # if os.path.exists(wavdir):
    #     files=os.listdir(wavdir)
    #     for file in files:
    #         os.remove(os.path.join(wavdir,file))
    
