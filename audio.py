
import pyaudio

import wave

from array import array

#import matplotlib.pyplot as plt

import statistics

import hub

import utime

from flask import Flask, Response, render_template

import serial

import sys

import os

 

ser = serial.Serial(

    port='/dev/serial0',

    baudrate = 115200,

    parity=serial.PARITY_NONE,

    stopbits=serial.STOPBITS_ONE,

    bytesize=serial.EIGHTBITS,

    timeout=1

)

os.chdir("/")

 

form_1 = pyaudio.paInt16 # 16-bit resolution

chans = 1 # 1 channel

samp_rate = 44100 # 44.1kHz sampling rate

chunk = 4096 # 2^12 samples for buffer

record_secs = 3 # seconds to record

dev_index = 1 # device index found by p.get_device_info_by_index(ii)

frames = []

deviation_data= []

 

audio = pyaudio.PyAudio() # create pyaudio instantiation

 

# create pyaudio stream

stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \

                    input_device_index = dev_index,input = True, \

                    frames_per_buffer=chunk)

print("recording")


 

while True:

    data = stream.read(chunk,exception_on_overflow = False)

    data = array('h',data).tolist()

    deviation = statistics.stdev(data)

    print(deviation)

    deviation_data.append(deviation)

 

    if deviation > 40:

        ser.write(("on").encode())

    else:

        ser.write(("off").encode())
