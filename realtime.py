# import ui_plot
import sys
import numpy as np
# from PyQt4 import QtCore, QtGui
# import PyQt4.Qwt5 as Qwt
from listen import *
from pylab import plot, show, title, xlabel, ylabel, subplot, savefig, xlim
import time



prevbit = -1
times = []
prevamp = 0
BITLENGTH = 170.0


def timesToBits(times):
    bitMessage = ''
    for i in range(len(times)-1):
        
        
        # bitMessage += str((i+1)%2)*numBits
        dt = times[i+1] - times[i]
        if i%2 == 0:
            numBits = int(round(dt/BITLENGTH))
            if numBits == 0:
                numBits = 1;
            print '1\t' + str(int(round(dt))) + '\t' + str(numBits)
            bitMessage += '1'*numBits
        else:
            # dt +=  27*dt/BITLENGTH
            numBits = int(round(dt/BITLENGTH))
            if numBits == 0:
                numBits = 1;
            print '0\t' + str(int(round(times[i+1] - times[i]))) + ':' + str(int(round(dt))) + '\t' + str(numBits)
            bitMessage += '0'*numBits
    return bitMessage


def plotSomething():
    global prevbit, times, prevamp, prevtime
    if listener.newAudio==False: 
        return
    xs,ys=listener.fft()
    # c.setData(xs,ys)
    # uiplot.qwtPlot.replot()
    # plot(xs,abs(ys),'r') # plotting the spectrum
    # xlabel('Freq (Hz)')
    # ylabel('|Y(freq)|')
    # listener.newAudio=False
    # show()
    xs = xs[5:]
    ys = ys[5:]
    amp = np.amax(ys)
    freq = xs.item(np.argmax(ys))
    # # if abs(freq - prevfreq) > 1: #88.4

    # if amp != prevamp:
    #     print str(freq) + ':\t' + str(amp)
    #     prevamp = amp

    if amp != prevamp:
        # print str(freq) + '\t' + str(amp)
        # print '\t\t\t\t' + str(freq) + '\t' + str(amp)
        prevamp = amp

        if amp > 2500 and abs(freq - 4000) < 100:
            currbit = 1
        elif prevbit != -1 and amp > 2500 and abs(freq - 3000) < 100:
            currbit = 0
        else:
            currbit = -1
            if prevbit != -1:
                print 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
                print '\t\t\t\t' + str(freq) + '\t' + str(amp)

        if len(times) > 0 and prevbit == -1 and  currbit == -1:
            times.append(time.clock()*1000)
            bits = timesToBits(times)[1:]
            # if len(bits)%8 != 0:
            #     bits = bits + '0'*(8 - len(bits)%8)
            bits = bits[:len(bits)-len(bits)%8]
            # bits = bits.ljust(8, '0') # pad with 0s on the right
            print [bits[i:i+8] for i in range(0, len(bits), 8)]
            message = ''.join([chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)])
            print message
            times = []
            prevbit = -1

        if currbit != prevbit:
            print str(prevbit) + "\t" + str(currbit)
            prevbit = currbit
            if currbit != -1:
                times.append(time.clock()*1000)
                print times
                if currbit == 0:
                    print times[-1] - times[-2]
                    if times[-1] - times[-2] < BITLENGTH/4:
                        # times = times[:-2]
                        print times
                    # print times[-1] - times[-2]
                    # print times


    """
        if the amplitude is large enough and it's the right freq
            if currbit is 0 # OFF TO ON
                record the time as prevtime
                currbit = 1
            if recording = False
                elif time passed/88.4 > 7.9 and recording == False
                    recording = True
                    prevtime = current time
            else (recording is True)
                
        else (not tone)
            if recording = True
                if currbit is 1 # ON TO OFF
                    numberOfBits
                    record the time as prevtime

    """         

    """
        times = []
        prevbit = 0

        if the amplitude is large enough and it's the right freq
            if prevbit is 0 # OFF TO ON
                append current time to times
                prevbit = 1
        else (not tone)
            if prevbit is 1 # ON TO OFF
                append current time to times
                prevbit = 0

    """

if __name__ == "__main__":
    # app = QtGui.QApplication(sys.argv)
    
    # win_plot = ui_plot.QtGui.QMainWindow()
    # uiplot = ui_plot.Ui_win_plot()
    # uiplot.setupUi(win_plot)
    # uiplot.btnA.clicked.connect(plotSomething)
    # #uiplot.btnB.clicked.connect(lambda: uiplot.timer.setInterval(100.0))
    # #uiplot.btnC.clicked.connect(lambda: uiplot.timer.setInterval(10.0))
    # #uiplot.btnD.clicked.connect(lambda: uiplot.timer.setInterval(1.0))
    # c=Qwt.QwtPlotCurve()  
    # c.attach(uiplot.qwtPlot)
    
    # uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.yLeft, 0, 1000)
    
    # uiplot.timer = QtCore.QTimer()
    # uiplot.timer.start(1.0)
    
    # win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething) 
    
    listener = Listener()
    listener.setup()
    listener.continuousStart()

    while True:
        plotSomething()

    ### DISPLAY WINDOWS
    # win_plot.show()
    # code=app.exec_()
    # listener.close()
    # sys.exit(code)