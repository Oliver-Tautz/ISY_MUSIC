import os.path

from scipy.io.wavfile import read as wav_read
from scipy.io.wavfile import write as wav_write
import scipy.signal
from tqdm import tqdm
import cv2
from subprocess import run
from os import environ, path, makedirs
import matplotlib.pyplot as plt
import numpy as np


if 'TMPDIR' in environ.keys():
    tmpdir=environ['TMPDIR']
else:
    tmpdir='/tmp'

# uses sox to downsample file. 
# stores file in $TMPDIR and removes after reading.
def downsample(filename,samplerate_new):
    samplerate_old, samples = wav_read(filename)


    tmpfile = path.join(tmpdir,f"{filename}")
    run(['sox',filename, '-r',str(samplerate_new),tmpfile])

    samplerate_down, downsamples = wav_read(tmpfile)

    assert samplerate_new == samplerate_down, "Downsampled file has wring samplerate"
    run(['rm',tmpfile])

    return downsamples

# returns dict of spectrograms. 
def spectrograms(filename,seconds=1,channels=[0,1],samplerate_new=None):

    specdir=f"{filename.split('.')[0]}_spectogramms"
    makedirs(specdir,exist_ok=True)
    specs=dict()

    # if new samplerate, downsample/upsample. Better use only downsampling!
    if samplerate_new:
        samplerate = samplerate_new

        samples=downsample(filename,samplerate_new)
    
    # else use file as is
    else:
        samplerate, samples = wav_read(filename)

    # len of the audio file in seconds
    len_in_secs = len(samples)/samplerate
    print(len_in_secs)
    
    # len_in_secs/seconds is the number of timesteps to make spectogramms
    timesteps = int(len_in_secs//seconds)
    print(timesteps)


    print('timestep',seconds*samplerate)
    # make specs for each channel.

    for c in channels:
        channel = samples[:,c]
        # specs for channel
        specs_c = [] 

        for i in tqdm(range(timesteps),desc='getting spectrograms!'):
            # start at timestep.
            start = samplerate*seconds*i
                
            # end one timestep later
            end = start+samplerate*seconds
            
            samples_slice = channel[start:end]
            #print(samples_slice.shape) 
            spec=scipy.signal.spectrogram(samples_slice,samplerate)
            specs_c.append(spec)
        
        # return dict with specs per channel
        specs[c] = specs_c
    return specs
    

#saves plot of spec=(f,t,sXX) to filename
def plot_spectrogram(spec_file,save_filename):
   # f,t,spec = spec
    #plt.pcolormesh(t,f,spec)
    print(spec_file)
    samplerate, samples = wav_read(spec_file)
    print(samples[:,0].shape)
    print(samplerate)
    plt.specgram(x=samples[:,0],Fs=samplerate)
    plt.savefig(save_filename,dpi=600)
    plt.clf()



#makes timecorret video of audiofile        
def make_video(filename,channel=0,timestep_in_seconds=5):


    filename_without_extension = filename.split('.')[0]

    sps = spectrograms(filename,channels=[channel],seconds=timestep_in_seconds)
    sps = sps[channel]

    # working directory
    workdirname = path.join(tmpdir,filename.split('.')[0])
    makedirs(workdirname,exist_ok=True)
    
    # savename for pngs
    generic_png_savename = path.join(workdirname,f"channel={channel}_timestep={timestep_in_seconds}s")
    videoname = path.join(tmpdir,f"{filename_without_extension}.mp4")


    

    # plot images
    for i,spec in tqdm(enumerate(sps),desc='plotting',total=len(sps)):
        savename = f"{generic_png_savename}_{str(i).zfill(3)}.png"
        plot_spectrogram(filename,savename)
        
    # use ffmpeg to make video
    run(['ffmpeg',
        '-framerate', f'1/{timestep_in_seconds}',
        '-i',f'{generic_png_savename}_%03d.png',
        '-i',filename,
        videoname])




path_str ='/data_ssd/music-demixing-challenge-starter-kit/small_data/test'

for song_dir in os.listdir(path_str):
    for filename in (['bass.wav','drums.wav','mixture.wav','other.wav','vocals.wav']):
        print(filename)
        make_video(os.path.join(path_str,song_dir,filename))
