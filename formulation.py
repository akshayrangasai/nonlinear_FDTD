from data import waveProperties, materialProperties
import numpy as np
import scipy as sp
import matplotlib as mp


#####################################################################
#Rules of code: Class elements always begin with a capital letter. Defaults are always allcaps. Arguments to functions to mimic class members.
######################################################################

class simulation:
    #Time is of type float; Dimensions is a list of floats.
    
    def __init__(self, MaterialProperties = None, WaveProperties = None, Time = None, Dimensions = None, Waveguide = None, Mesh = None):
        
        if material is None:
            self.MaterialProperties = materialProperties()
        else:
            self.MaterialProperties = MaterialProperties
        
        if wave is None:
            self.WaveProperties = waveProperties()
        else:
            self.WaveProperties = WaveProperties
        
        if Time is None:
            self.Time = df.TIME
        else:
            self.Time = Time
        
        if Dimensions is None:
            self.Dimensions = df.DIMENSIONS
        else:
            self.Dimensions = Dimensions
            
        if self.WaveGuide is None:
            self.WaveGuide = df.WAVEGUIDE
        else:
            self.WaveGuide = WaveGuide
        
        if self.Mesh is None:
            self.Mesh = df.MESH
        else:
            self.Mesh = Mesh
    
        #1D, 2D or 3D 
        self.DimensionCount = len(self.Dimensions)
##        self.WaveProperties.WaveVelocity = self.MaterialProperties.WaveVelocity
        self.WaveProperties.WaveLength = (float) (self.MaterialProperties.WaveVelocity/self.WaveProperties.Frequency)
        
        self.Dx = setMesh()
        ##List of elements
        self.ElementSpan = [X/self.Dx for X in self.Dimensions]
         
        self.Grid = sp.zeroes(tuple(self.ElementSpan), float)
        
    def setMesh(self):
        
        if self.Mesh == 0:
            return (float)(self.WaveProperties.Wavelength/8.0)
        elif self.Mesh == 1:
            return (float)(self.WaveProperties.Wavelength/24.0)
        elif self.Mesh == 2:
            return (float)(self.WaveProperties.Wavelength/64.0)
        else:
            return (float)(self.WaveProperties.Wavelength/128.0)
       
        
