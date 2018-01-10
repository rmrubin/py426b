#!/usr/bin/env python

"""


"""

from tools import dds, wav

__version__ = "0.2"
__status__ = "Development"
__author__ = "Randy Rubin"

WAV_FILENAME = 'py426b-track01-cal_tone_1khz_sine_-6dbfs_peak.wav'
SIGNAL_FREQ = 1000.0
SIGNAL_LEN = 60.0

buffer = dds.pure_tone(SIGNAL_FREQ, SIGNAL_LEN)
wav.write(buffer, WAV_FILENAME)
