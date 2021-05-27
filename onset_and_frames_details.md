# Details of onset and frames pytorch data

## example:

audio_length: 22567994

begin = random(audio_length-self.sequence_length) // HOP_LENGTH (31434)
nsteps = sequence_length/ HOP_LENGTH              (640)
step_end = step_begin + nsteps                    (32074)

begin = step_begin * HOPLENGTH                    (16094208)
end = begin + self.sequence_length                (16421888)

audio = data['audio'][begin:end]                  (327680) sequence_length


## What does it mean?

So input=audio file of arbitrary **audio_length** with **sample_rate = 16k**

find random starthop < **audio_length**-**sequence_length=327680**//**HOPSIZE**

Cut out audio for begin-end, line up with midi! . So **640 steps** of **HOPSIZE=512** of per spectrogramm

## Spectogramm properties

**640 steps**  of **HOPSIZE=512**
**229** frequencies with difference **WINDOW_LENGTH=2048** (??? This is still unclear to me. What is fmin=30,fmax=8000)

So spectogramm covers 512*16000 = about 20s .
Hopsize is 512/16000 = about 0.032s


## BiLSTM

I cant find the states resetting. Two hypothesis: 
* No reset. (highly unlikely)
* Reset after each batch. Some magic inside nn.Sequential?!

* LSTM has 768 timesteps with 384 dimensional hidden state. This can be adjusted in model creation


