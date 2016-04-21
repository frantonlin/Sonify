import pyaudio
# import numpy as np
import math

FREQUENCY = 1000
BITRATE = 48000
DATASIZE = 4096

PyAudio = pyaudio.PyAudio
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)
                                
def generate_tone(frequency, bit):
    if bit:
        return ''.join([chr(int(math.sin(x/((BITRATE/frequency)/math.pi))*127+128)) for x in xrange(DATASIZE)])
    else:
        return ''.join([chr(128) for x in xrange(DATASIZE)])

print "Type a message"
while(1):
    text = raw_input(": ")
    message = map(bin, bytearray(text))
    print message
    message = '11111111'.join([item[2:] for item in message])
    message = '11111111' + message
    print message
    # freqs = [int(bit)*FREQUENCY for bit in message]
    # print freqs
    wavedata = ''.join([generate_tone(FREQUENCY, int(bit)) for bit in message])
    # print wavedata
    stream.write(wavedata)
    
stream.stop_stream()
stream.close()
p.terminate()