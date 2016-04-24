import pyaudio
import math
import time

FREQUENCY = 2000
BITRATE = 48000
DATASIZE = 2**13

PyAudio = pyaudio.PyAudio
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)
                                
def generate_tone(frequency, bit, numBits):
    print str(bit) + '\t' + str(numBits)
    if bit:
        return ''.join([chr(int(math.sin(x/((BITRATE/frequency)/math.pi))*127+128)) for x in xrange(DATASIZE*numBits)])
    else:
        # return ''.join([chr(128) for x in xrange(DATASIZE*numBits)])
        return ''.join([chr(int(math.sin(x/((BITRATE/1500)/math.pi))*127+128)) for x in xrange(DATASIZE*numBits)])

print "Type a message"
while(1):
    text = raw_input(": ")
    message = map(bin, bytearray(text))

    print [item[2:].zfill(8) for item in message]
    message = ''.join([item[2:].zfill(8) for item in message])
    message = '1' + message
    # print message
    # freqs = [int(bit)*FREQUENCY for bit in message]
    # print freqs
    wavedata = ''
    bit = 1
    while len(message) > 0:
        # print message + '\t' + str(bit)
        # print bit
        numBits = message.find(str(bit^1)) # look for opposite bit
        if numBits == -1:
            numBits = len(message)
        wavedata += generate_tone(FREQUENCY, bit, numBits)
        message = message[numBits:]
        bit ^= 1 # bitwise XOR statement
        
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