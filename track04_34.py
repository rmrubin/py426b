#!/usr/bin/env python

"""Pure Tones for Distortion Tests (Tracks 4 – 34)

Specification
The standard specifies that the CD contain pure tones for distortion
testing at all the IEC standard one-third-octave center frequencies
ranging from 20 Hz to 5 kHz. These tracks are to contain 15
seconds of tone followed by 5 seconds of silence and be recorded
at a level equal to the calibration tone on track 1.
For completeness, I choose to include the rest of the pure tones on
the CD ranging from 6.3 kHz to 20 kHz as bonus tracks.

Development
As with the calibration tone on track 1, the peak level of each tone
was set to –6 dB which corresponds to a maximum count of
±16,384 for the sinewave. For each tone, the signal was on for 15
seconds and off for 5 making a total track time of 20 seconds. A
four-cycle half-Hann ramp was added to the start and finish of
each tone to minimize start/stop transients (see Fig. 1 for an
example of four-cycle half-Hann ramps added to a signal at the
beginning and end).
"""

__version__     = "0.1"
__status__      = "Development"
__author__      = "Randy Rubin"


import numpy as np
from tools import dds, wav


FILENAME_PRE = 'py426b-track'
FILENAME_MID = '-pure_tone_'
FILENAME_POST = 'hz_-6dbfs_peak.wav'

TONE_LEN = 15.0
SILENCE_LEN = 5.0
FIRST_TRACK = 4

silence = np.zeros(int(round(dds.SAMPLE_RATE * SILENCE_LEN)), dtype=np.int16)

freq_tab = [
    20.0,
    25.0,
    31.5,
    40.0,
    50.0,
    63.0,
    80.0,
    100.0,
    125.0,
    160.0,
    200.0,
    250.0,
    315.0,
    400.0,
    500.0,
    630.0,
    800.0,
    1000.0,
    1250.0,
    1600.0,
    2000.0,
    2500.0,
    3150.0,
    4000.0,
    5000.0,
    6300.0,
    8000.0,
    10000.0,
    12500.0,
    16000.0,
    20000.0,
]

for i in range(len(freq_tab)): 
    buffer = dds.pure_tone(freq_tab[i], TONE_LEN)
    buffer = np.concatenate([buffer, silence])
    filename = '{}{:02d}{}{:g}{}'.format(FILENAME_PRE, FIRST_TRACK+i,
                                         FILENAME_MID, freq_tab[i],
                                         FILENAME_POST)
    wav.write(buffer, filename)
