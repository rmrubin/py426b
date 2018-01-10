#!/usr/bin/env python

"""


"""

import numpy as np

from tools import dds, wav

__version__ = "0.1"
__status__ = "Development"
__author__ = "Randy Rubin"

FILENAME_PRE = 'py426b-track'
FILENAME_MID = '-pure_tone_'
FILENAME_POST = 'hz_-6dbfs_peak.wav'

SAMPLE_RATE = dds.SAMPLE_RATE
TONE_LEN = 15.0
SILENCE_LEN = 5.0
FIRST_TRACK = 4

silence = np.zeros(int(round(SAMPLE_RATE * SILENCE_LEN)), dtype=np.int16)

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
