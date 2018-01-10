#!/usr/bin/env python

"""


"""

import numpy as np

from tools import dds, wav

__version__ = "0.1"
__status__ = "Development"
__author__ = "Randy Rubin"

FILENAME_PRE = 'py426b-track'
FILENAME_MID = '-tone_burst_'
FILENAME_POST = 'hz_-6dbfs_peak.wav'

SAMPLE_RATE = dds.SAMPLE_RATE
BURST_CYCLES = 6.5
LCH_REPEAT_SEC = 1.0
RCH_REPEAT_SEC = 10.0
TRACK_LEN_SEC = 30.0
FIRST_TRACK = 35

freq_tab = [
    10.0,
    12.5,
    16.0,
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

    buffer = dds.tone_burst(freq_tab[i], (1 / freq_tab[i]) * BURST_CYCLES)

    lch = np.copy(buffer)
    rch = np.copy(buffer)
    lch.resize(int(round(SAMPLE_RATE * LCH_REPEAT_SEC)))
    rch.resize(int(round(SAMPLE_RATE * RCH_REPEAT_SEC)))
    lch = np.tile(lch, int(round(TRACK_LEN_SEC / LCH_REPEAT_SEC)))
    rch = np.tile(rch, int(round(TRACK_LEN_SEC / RCH_REPEAT_SEC)))

    buffer = wav.mono2stereo(lch, rch)

    filename = '{}{:02d}{}{:g}{}'.format(FILENAME_PRE, FIRST_TRACK+i,
                                         FILENAME_MID, freq_tab[i],
                                         FILENAME_POST)
    wav.write(buffer, filename, chans=2)
