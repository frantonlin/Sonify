import pyaudio
# import numpy as np
import math

FREQUENCY = 2000
BITRATE = 48000
DATASIZE = 1024

PyAudio = pyaudio.PyAudio
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)

print "Type a message"
while(1):
    text = raw_input(": ")
    message = map(bin, bytearray(text))
    message = '1111111'.join([item[2:] for item in message])
    # freqs = [int(bit)*FREQUENCY for bit in message]
    # print freqs
    wavedata = ''.join([generate_tone(FREQUENCY, bit) for bit in message])
    stream.write(wavedata)




def generate_tone(frequency, bit):
    if bit:
        return ''.join([chr(int(math.sin(x/((BITRATE/frequency)/math.pi))*127+128)) for x in xrange(BITRATE)])
    else:
        return ''.join([chr(128) for x in xrange(BITRATE)])