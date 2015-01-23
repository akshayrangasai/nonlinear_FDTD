import numpy as np
import scipy as sp
import pylab
import os

__DIR = "./data/sensitivity"
__STARTINDEX = 4900
__ENDINDEX = 5600
__PADDING = 1348

files = [os.path.join(__DIR,f) for f in os.listdir(__DIR)]
for f in files:
    sp.io.readmat(f)

