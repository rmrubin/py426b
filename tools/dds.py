#!/usr/bin/env python

"""


"""

__version__     = "0.2"
__status__      = "Development"
__author__      = "Randy Rubin"

import numpy as np
from tools import env, wav


SAMPLE_RATE = wav.SAMPLE_RATE
SAMPLE_MAX = int(round(2**14))
PURE_TONE_FADE_SEC = 0.004


_PHASE_BITS = 64
_INDEX_BITS = 16 
_ACC_SHIFT = np.uint64(_PHASE_BITS - _INDEX_BITS)


def init(amp=SAMPLE_MAX):

    sintab = np.empty(2**_INDEX_BITS, dtype=np.int16)

    for i in range(sintab.size):
        sintab[i] = int(round(amp*np.sin(2*np.pi*(i/sintab.size))))

    phase = np.uint64(0)

    return phase, sintab


def tuning(freq, fs=SAMPLE_RATE, bits=_PHASE_BITS):

    return np.uint64(int(round((freq / fs) * 2**bits)))


def inc_phase(phase, tuning_word):

    np.uint64(phase)
    np.uint64(tuning_word)
    phase += tuning_word

    return phase


def get_sample(phase, wavtab):

    return wavtab[phase >> _ACC_SHIFT]


def gen_tone(freq, length, amp=SAMPLE_MAX, fs=SAMPLE_RATE):

    buffer = np.empty(length, dtype=np.int16)

    phase, wavtab = init(amp)
    tuning_word = tuning(freq, fs)

    for i in range(buffer.size):
        buffer[i] = get_sample(phase, wavtab)
        phase = inc_phase(phase, tuning_word)

    return buffer


def pure_tone(freq, length, amp=SAMPLE_MAX, fs=SAMPLE_RATE):

    # generate signal
    buffer_len = int(round(fs * length))
    buffer = gen_tone(freq, buffer_len, amp, fs)

    # apply hann fade in and out
    fade_len = int(round(fs * PURE_TONE_FADE_SEC))
    buffer = env.hann_in(buffer, fade_len)
    buffer = env.hann_out(buffer, fade_len)

    return buffer


def tone_burst(freq, length, amp=SAMPLE_MAX, fs=SAMPLE_RATE):

    # generate signal
    buffer_len = int(round(fs * length))
    buffer = gen_tone(freq, buffer_len, amp, fs)

    # apply hann envelope
    buffer = env.hann_all(buffer)

    return buffer
