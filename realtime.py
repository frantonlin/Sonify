# import ui_plot
import sys
import numpy as np
# from PyQt4 import QtCore, QtGui
# import PyQt4.Qwt5 as Qwt
from listen import *
from pylab import plot, show, title, xlabel, ylabel, subplot, savefig, xlim
import time



prevbit = 0
times = []


def plotSomething():
    global prevbit, times
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
    maxAmp = np.amax(ys)
    freq = xs.item(np.argmax(ys))
    # if abs(freq - prevfreq) > 1: #88.4
    if maxAmp > 8000 and abs(freq - 1000) < 20:
        currbit = 1
    else:
        currbit = 0

    if currbit != prevbit:
        times.append(time.clock()*1000)
        if currbit == 0:
            print times[-1] - times[-2]
        prevbit = currbit

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