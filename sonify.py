import pyaudio
import math
import time

FREQUENCY = 2000
BITRATE = 48000
DATASIZE = 2**14
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
    # item = (len(item)-8)*"0" + item
    message = ''.join([item[2:].zfill(8) for item in message])
    message = '1' + message
    print message
    # freqs = [int(bit)*FREQUENCY for bit in message]
    # print freqs
    wavedata = ''.join([generate_tone(FREQUENCY, int(bit)) for bit in message])
    # print wavedata
    # start = time.time()
    stream.write(wavedata)
    # end = time.time()
    # print end-start
    
stream.stop_stream()
stream.close()
p.terminate()


"""

while (true):
    currBit = readBit

    if currBit != prevBit
        times.append(time.time())

    prevBit = currBit

"""