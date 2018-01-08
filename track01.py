#!/usr/bin/env python

"""Amplitude Calibration Tone (Track 1) 

Specification
Track 1 is specified to contain a 1000-Hz constant-amplitude
calibration tone that lasts for one minute (60 seconds). The tone is
intended for use as an amplitude calibration signal for all the test
signals that follow on the disk. The following power-compression
swept-sine signal and distortion test tones are recorded at the same
level as the calibration tone, and the life-test noise signal is
recorded at an rms level 3-dB lower than the calibration tone. A
ramp is specified to reduce pops and clicks.

Development
The specification was followed exactly with the peak level set to 6-
dB down referenced to the CD’s 16-bit digital maximum of
±32,767 counts (0 dBFS). The –6-dB-peak level corresponds to a
maximum count of ±16,384 for the sinewave. The resultant rms
level of the sinewave is therefor –9 dBFS. A four-cycle half-Hann
ramp was added to the start and finish of the tone to minimize
start/stop transients. Signal length was set to 60 seconds. 
"""

__version__     = "0.2"
__status__      = "Development"
__author__      = "Randy Rubin"


from tools import dds, wav

WAV_FILENAME = 'py426b-track01-cal_tone_1khz_sine_-6dbfs_peak.wav'
SIGNAL_FREQ = 1000.0
SIGNAL_LEN = 60.0

buffer = dds.pure_tone(SIGNAL_FREQ, SIGNAL_LEN)
wav.write(buffer, WAV_FILENAME)
