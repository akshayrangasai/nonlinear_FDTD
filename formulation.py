from data import waveProperties, materialProperties
import numpy as np
import scipy as sp
import matplotlib as mp
import defaults as df
from solver import Solver as sl

#####################################################################
#Rules of code: Class elements always begin with a capital letter. Defaults are always allcaps. Arguments to functions to mimic class members.
######################################################################

class simulation:
    
    def setStep(self, Dx):
        #Courant Condition check
        return (Dx/self.MaterialProperties.WaveVelocityL)/2
      
    def setMesh(self):
        
        if self.Mesh == 0:
            return (float)(self.WaveProperties.WaveLength/8.0)
        elif self.Mesh == 1:
            return (float)(self.WaveProperties.WaveLength/24.0)
        elif self.Mesh == 2:
            return (float)(self.WaveProperties.WaveLength/64.0)
        else:
            return (float)(self.WaveProperties.WaveLength/128.0)
    
    #Time is of type float; Dimensions is a list of floats.
    
    
    def __init__(self, MaterialProperties = None, WaveProperties = None, Time = None, Dimensions = None, WaveGuide = None, Mesh = None):
        
        if MaterialProperties is None:
            self.MaterialProperties = materialProperties()
        else:
            self.MaterialProperties = MaterialProperties
        
        if WaveProperties is None:
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
            
        if WaveGuide is None:
            self.WaveGuide = df.WAVEGUIDE
        else:
            self.WaveGuide = WaveGuide
        
        if Mesh is None:
            self.Mesh = df.MESH
        else:
            self.Mesh = Mesh
    
        #1D, 2D or 3D 
        self.DimensionCount = len(self.Dimensions)
##        self.WaveProperties.WaveVelocity = self.MaterialProperties.WaveVelocity
        self.WaveProperties.WaveLength = (float) (self.MaterialProperties.WaveVelocityL/self.WaveProperties.Frequency)
        
        self.Dx = self.setMesh()
        self.Dt = self.setStep(self.Dx)
        
        #print self.Dx
        ##List of elements
        self.ElementSpan = [round(X/self.Dx) for X in self.Dimensions]
        
        #Append Dimensions
        self.ElementSpan.append(3) 
        #Append Times
        self.ElementSpan.append(3)
        
        self.Grid = sp.zeros(tuple(self.ElementSpan), float)
        
    
sim = simulation()
solution = sl(sim)
