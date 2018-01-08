#!/usr/bin/env python

"""


"""

__version__     = "0.2"
__status__      = "Development"
__author__      = "Randy Rubin"

import numpy as np
import wave as wv

WAV_FILENAME = 'default.wav'
SAMPLE_RATE = 44100
CHANNELS = 1
SAMPLE_BYTES = 2

def write(data, filename=WAV_FILENAME,
            fs=SAMPLE_RATE, chans=CHANNELS, sample_bytes=SAMPLE_BYTES):
    wf = wv.open(str(filename), 'w')
    wf.setnchannels(int(round(chans)))
    wf.setsampwidth(int(round(sample_bytes)))
    wf.setframerate(int(round(fs)))
    wf.writeframes(data)
    wf.close()

def mono2stereo(lch, rch):
    buffer = np.empty(lch.size*2, dtype=np.int16)
    for i in range(lch.size):
        buffer[2*i] = lch[i]
        buffer[2*i+1] = rch[i] 
    return buffer
