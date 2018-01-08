#!/usr/bin/env python

"""


"""

__version__     = "0.2"
__status__      = "Development"
__author__      = "Randy Rubin"

import numpy as np
from scipy.signal import hann

def hann_in(data, duration):
    buffer = np.copy(data)
    envtab = hann(duration*2)
    for i in range(duration):
        buffer[i] = int(round(buffer[i]*envtab[i]))
    return buffer

def hann_out(data, duration):
    buffer = np.copy(data)
    envtab = hann(duration*2)
    fade_start = buffer.size - duration
    for i in range(duration):
        buffer[fade_start+i] = int(round(buffer[fade_start+i]*envtab[duration+i]))
    return buffer

def hann_all(data):
    buffer = np.copy(data)
    envtab = hann(data.size)
    for i in range(data.size):
        buffer[i] = int(round(buffer[i]*envtab[i]))
    return buffer
