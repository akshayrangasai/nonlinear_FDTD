from data import waveProperties, materialProperties
import numpy as np
import scipy as sp
import matplotlib as mp

class simulation(waveProperties, materialProperties):
    def setWaveProperties(self, Frequency = None)
        if Frequency is not None:
            self.Frequency = Frequency
        else
            self.Frequency = FREQUENCY
    
