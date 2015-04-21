import numpy as np
import scipy.io as sp
from matplotlib import pyplot as plt
import os

__DIR = "./data/sensitivity/tentoten"
__TOTALLENGTH = 2048
__STARTINDEX = 4900
__ENDINDEX = 5600
__PADDING = __TOTALLENGTH - (__ENDINDEX - __STARTINDEX)
__FILE = "amplitude_BetaT1010.txt"
files = [os.path.join(__DIR,f) for f in os.listdir(__DIR)]

fi = open(__FILE,'w+')


def fft(signal):
    fftsignal = np.zeros(__TOTALLENGTH)
    #fftsignal[0:(__TOTALLENGTH - __PADDING)] = signal[__STARTINDEX:__ENDINDEX]
    fftsignal_2 = signal[__STARTINDEX:__ENDINDEX]
    ftp = abs(np.fft.fft(fftsignal_2))
    plot = plt.plot(ftp)
    return plot
            
def ampcalc(data):
    return abs(min(data) - max(data))

for f in files:
    print f.split('/')
    datafile = sp.loadmat(f)
    fftplot = fft(datafile['SourceSignal'])
    amplitude = ampcalc(datafile['SourceSignal'])
    plt.savefig("%s.png"%f.split('/')[4])
    plt.close()
    fi.write('%s - %.25f\n'%(f.split('/')[4], amplitude))
