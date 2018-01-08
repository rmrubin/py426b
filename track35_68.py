#!/usr/bin/env python

"""Shaped Tone Bursts for Peak Power and Headroom Tests (Tracks 35 – 68)

Specification

Additional bonus tracks were included on the CD which contain
6.5-cycle shaped tone bursts whose energy is constrained to a one-
third-octave bandwidth. These bursts are intended for use as a test
stimulus  for  frequency-dependent  short-term  peak  power
assessment and headroom of loudspeakers and electronics, and for
testing the frequency response, energy decay and narrow-band
phase/polarity of systems.

The tone burst tracks should cover the frequency range from 10 Hz
to 20 kHz at all the preferred IEC standard one-third-octave center
frequencies. The bursts are repeated at one burst per second on the
left channel and one burst per 10 seconds (0.1 burst per second) on
the right channel. Each track lasts for 30 seconds. The low-
repetition rate on the right channel makes these signals more
suitable for systems that have long energy decay (reverberation)
times such as large rooms and concert halls.
"""

__version__     = "0.1"
__status__      = "Development"
__author__      = "Randy Rubin"


import numpy as np
from tools import dds, wav


FILENAME_PRE = 'py426b-track'
FILENAME_MID = '-tone_burst_'
FILENAME_POST = 'hz_-6dbfs_peak.wav'

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
    lch.resize(int(round(dds.SAMPLE_RATE * LCH_REPEAT_SEC)))
    rch.resize(int(round(dds.SAMPLE_RATE * RCH_REPEAT_SEC)))
    lch = np.tile(lch, int(round(TRACK_LEN_SEC / LCH_REPEAT_SEC)))
    rch = np.tile(rch, int(round(TRACK_LEN_SEC / RCH_REPEAT_SEC)))

    buffer = wav.mono2stereo(lch, rch)

    filename = '{}{:02d}{}{:g}{}'.format(FILENAME_PRE, FIRST_TRACK+i,
                                         FILENAME_MID, freq_tab[i],
                                         FILENAME_POST)
    wav.write(buffer, filename, chans=2)
