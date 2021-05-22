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

find random starthop < **audio_length**-**sequence_length=327680**//**HOP_LENGTH**
Cut out audio for 


