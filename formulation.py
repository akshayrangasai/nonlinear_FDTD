from data import waveProperties, materialProperties
import numpy as np
import scipy as sp
import matplotlib as mp
import defaults as df
import sys
from solver import Solver as sl
import scipy.io as sio
from matplotlib.pyplot import plot,figure
   

#####################################################################
#Rules of code: Class elements always begin with a capital letter. Defaults are always allcaps. Arguments to functions to mimic class members.
######################################################################

class simulation:
    
    def setMixing(self, val):
        self.Mixing = val

    def setStep(self, Dx):
        #Courant Condition check
        return (Dx/self.MaterialProperties.WaveVelocityL)/2
      
    def setMesh(self):
        
        if self.Mesh == 0:
            return (float)(self.WaveProperties.WaveLength/8.0)
        elif self.Mesh == 1:
            return (float)(self.WaveProperties.WaveLength/12.0)
        elif self.Mesh == 2:
            return (float)(self.WaveProperties.WaveLength/64.0)
        elif self.Mesh == 3:
            return (float)(self.WaveProperties.WaveLength/128.0)
    
    #Time is of type float; Dimensions is a list of floats.
    
    
    def setParam(self, paramName, value):
        
        if paramName == 'l':
            self.MaterialProperties.l = value
        if paramName == 'm':
            self.MaterialProperties.m = value


    def getParam(self, paramName):
        
        if paramName == 'l':
            return self.MaterialProperties.l
        if paramName == 'm':
            return self.MaterialProperties.m

        return 0
    
    
    def __init__(self, MaterialProperties = None, WaveProperties = None, Reflections = None, Dimensions = None, WaveGuide = None, Mesh = None, Pulses = None):
        
        if MaterialProperties is None:
            self.MaterialProperties = materialProperties()
        else:
            self.MaterialProperties = MaterialProperties
        
        if WaveProperties is None:
            self.WaveProperties = waveProperties()
        else:
            self.WaveProperties = WaveProperties
        
        if Reflections is None:
            self.Reflections = df.REFLECTIONS
        else:
            self.Reflections = Reflections
        
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
            
        if Pulses is None:
            self.Pulses = df.PULSES
        else:
            self.Pulses = Pulses
        
        self.Time = 2*self.Reflections*self.Dimensions[1]/self.MaterialProperties.WaveVelocityL
    
        #1D, 2D or 3D 
        self.DimensionCount = len(self.Dimensions)
##        self.WaveProperties.WaveVelocity = self.MaterialProperties.WaveVelocity
        self.WaveProperties.WaveLength = (float) (self.MaterialProperties.WaveVelocityL/self.WaveProperties.Frequency)
        self.Mixing = False 
        self.Dx = self.setMesh()
        self.Dt = self.setStep(self.Dx)
        
        #print self.Dx
        ##List of elementsb
        self.ElementSpan = [round(X/self.Dx) for X in self.Dimensions]
        
        #Append Dimensions
        self.ElementSpan.append(3) 
        #Append Times
        self.ElementSpan.append(3)
        
        self.Grid = sp.zeros(tuple(self.ElementSpan), float)
        self.NLGrid = sp.zeros(tuple(self.ElementSpan), float)
    	self.SourceSignal = sp.zeros((round(self.Time/self.Dt),1))
    	self.SData = sp.zeros((round(self.Time/self.Dt),1))
        self.ViewMovie = False
        self.viewPlot = True
    
def __init__():
    args = sys.argv    
    args = [arg.replace('--','') for arg in args]
    names = []
    sim = simulation()
    print sim.Dt
    if 'mixing' in args:
        sim.setMixing(True)
    if 'movie' in args:
        sim.ViewMovie = True
    solution = sl(sim)
    
    if 'noplot' in args:
        pass
    else:
        figure(5)
        plot(sim.SData)        
    
    if 'save' in args:
        try:
            ind = args.index('savenames')
            names.append(args[ind+1])
            names.append(args[ind+2])
        except:
            print "Using Default File names to save data"
            names.append("TotalSignal")
            names.append("NLinSignal")
        sio.savemat(names[0],{names[0]:sim.SourceSignal}) 
        sio.savemat(names[1],{names[1]:sim.SData})



if __name__ == "__main__":
    __init__()
