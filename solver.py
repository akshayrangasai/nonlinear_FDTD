import numpy as np
import scipy as sp
import defaults as df
from math import sin, pi, cos
from matplotlib.pyplot import imshow, plot, show, draw, pause, clim, figure
#from matplotlib import figure
class Solver:

    Simulation = None
    Location = None
    Width = None
    #Create a Movie Variable to calculate number of movies and plots, to bring them up when necessary. add arguments to put it in grid, instead of what's happening here. This is hardcoded waste.
    def putMovie(self, pauseTime):
        data = np.reshape(self.Simulation.Grid[:,:,0,1],  (self.Simulation.ElementSpan[0],self.Simulation.ElementSpan[1]))       #       # 
        figure(0)
        imshow(data)
        clim([-1e-8,1e-8])
        draw()
        pause(pauseTime)
        figure(1)
        data = np.reshape(self.Simulation.NLGrid[:,:,0,1],  (self.Simulation.ElementSpan[0],self.Simulation.ElementSpan[1]))       #       # 
        imshow(data)
        clim([-1e-13,1e-13])
        draw()
        pause(pauseTime)
        
            
    def putSource(self, i):
        
        #Adding default Source
        X_S = round(self.Location[0])  + 5 
        Y_S = slice(round(self.Simulation.ElementSpan[1]/2) - round(self.Width[0]/2), round(self.Simulation.ElementSpan[1]/2) + round(self.Width[0]/2))
        #self.Simulation.Grid[-1,Y_S,0,2] = (1- cos(2*pi*self.Simulation.WaveProperties.Frequency*i*self.Simulation.Dt))*cos(2*pi*self.Simulation.WaveProperties.Frequency*i*self.Simulation.Dt)*10e-8
        self.Simulation.Grid[X_S,Y_S,1,2] = sin(2*pi*self.Simulation.WaveProperties.Frequency*i*self.Simulation.Dt)*10e-8
        #print self.Simulation.Grid[X_S, round(self.Simulation.ElementSpan[1]/2) - round(self.Width[0]/2) + 1,0,2]
            
    #Line Sources only, currently. Multiple Sources must be accounted for, Must think of a matrix solution. So much fight for something that might not even work. Pain.
    def setSource(self, Location = None, Width = None, Theta = None) :
        
        if Location is None:
            self.Location = [df.LOCATION*self.Simulation.Dimensions[0]/self.Simulation.Dx]
        else:
            self.Location.append(Location*self.Simulation.Dimensions[0]/self.Simulation.Dx)

        if Width is None:
            self.Width = [(df.WIDTH/self.Simulation.Dx)*D for D in self.Simulation.Dimensions]
        else:
            self.Width.append((Width/self.Simulation.Dx)*D for D in self.Simulation.Dimensions)
            
        if Theta is None:
            self.Location = [df.THETA]
        else:
            self.Location.append(Theta)

        
    
    def Solve(self):
        #First Equation We'll be solving will be the standard wave equation.
        self.setSource()
        #Setting the Source first. Now, let's solve the DE like a boss
        
        _X = slice(0,self.Simulation.ElementSpan[0]-2)
        X = slice(1,self.Simulation.ElementSpan[0]-1)
        X_ = slice(2,self.Simulation.ElementSpan[0])
        
        _Y = slice(0,self.Simulation.ElementSpan[1]-2)
        Y = slice(1,self.Simulation.ElementSpan[1]-1)
        Y_ = slice(2,self.Simulation.ElementSpan[1])

        #_X indicates previous X coordinate and X_ indicts the one after
        r_var = round(self.Simulation.Time/self.Simulation.Dt)
        print "Total Iterations are " , r_var
        for i in range(1,int(r_var)):
            #Solving for Displacements in the X direction
            self.Simulation.Grid[X,Y,0,2] = 2*self.Simulation.Grid[X,Y,0,1] - self.Simulation.Grid[X,Y,0,0] + (pow(self.Simulation.Dt,2)/self.Simulation.MaterialProperties.Rho)*(
           
            (self.Simulation.MaterialProperties.Mu/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X_,Y,0,1] -2*self.Simulation.Grid[X,Y,0,1] + self.Simulation.Grid[_X,Y,0,1]) + ((self.Simulation.MaterialProperties.Mu/3 + self.Simulation.MaterialProperties.K)/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X_,Y,0,1] -2*self.Simulation.Grid[X,Y,0,1] + self.Simulation.Grid[_X,Y,0,1])
           + 
            (self.Simulation.MaterialProperties.Mu/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X,Y_,0,1] -2*self.Simulation.Grid[X,Y,0,1] + self.Simulation.Grid[X,_Y,0,1]) + ((self.Simulation.MaterialProperties.Mu/3 + self.Simulation.MaterialProperties.K)/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X_,Y_,1,1] -self.Simulation.Grid[X_,_Y,1,1] + self.Simulation.Grid[_X,_Y,1,1] - self.Simulation.Grid[_X,Y_,1,1])/4
           ) 
            #Solving for Y
            
            #self.Simulation.Grid[X,Y,1,2] = 2*self.Simulation.Grid[X,Y,1,1] - self.Simulation.Grid[X,Y,1,0] + (pow(self.Simulation.Dt,2)/self.Simulation.MaterialProperties.Rho)*(
            
            #(self.Simulation.MaterialProperties.Mu/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X,_Y,1,1] -2*self.Simulation.Grid[X,Y,1,1] + self.Simulation.Grid[X,_Y,1,1]) + ((self.Simulation.MaterialProperties.Mu/3 + self.Simulation.MaterialProperties.K)/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X,Y_,1,1] -2*self.Simulation.Grid[X,Y,1,1] + self.Simulation.Grid[X,_Y,1,1])
            #+ 
            #(self.Simulation.MaterialProperties.Mu/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X_,Y,1,1] -2*self.Simulation.Grid[X,Y,1,1] + self.Simulation.Grid[_X,Y,1,1]) + ((self.Simulation.MaterialProperties.Mu/3 + self.Simulation.MaterialProperties.K)/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X_,Y_,0,1] -self.Simulation.Grid[X_,_Y,0,1] + self.Simulation.Grid[_X,_Y,0,1] - self.Simulation.Grid[_X,Y_,0,1])/4
           #) 
            #Space for adding source. Must figure out modular solution. add as setSource function?
            if(i <= round((1.0/(self.Simulation.WaveProperties.Frequency))/self.Simulation.Dt)):
                self.putSource(i)
            else:
                pass #self.putSource(0)            
            #Space for adding boundary conditions. Create a setBoundary Condition. Should be peaceful
            
            #self.putBoundary()
            #Starting Non-linear stuff.
            
            self.Simulation.NLGrid[X,Y,0,2] = 2*self.Simulation.NLGrid[X,Y,0,1] - self.Simulation.NLGrid[X,Y,0,0] + pow(self.Simulation.Dt,2)*(pow(self.Simulation.MaterialProperties.WaveVelocityL ,2)*((self.Simulation.NLGrid[X_,Y,0,1] - 2*self.Simulation.NLGrid[X,Y,0,1] + self.Simulation.NLGrid[_X,Y,0,1])/pow(self.Simulation.Dx,2)) + pow(self.Simulation.MaterialProperties.BetaL,1)*((self.Simulation.Grid[X_,Y,0,1] - 2*self.Simulation.Grid[X,Y,0,1] + self.Simulation.Grid[_X,Y,0,1])*(self.Simulation.Grid[X_,Y,0,1] - self.Simulation.Grid[_X,Y,0,1])/(2*pow(self.Simulation.Dx,3))) + pow(self.Simulation.MaterialProperties.BetaT,1)*((self.Simulation.Grid[X_,Y,1,1] - 2*self.Simulation.Grid[X,Y,1,1] + self.Simulation.Grid[_X,Y,1,1])*(self.Simulation.Grid[X_,Y,1,1] - self.Simulation.Grid[_X,Y,1,1])/(2*pow(self.Simulation.Dx,3))))
            
           
           #Nonlinearity in Y
            
            self.Simulation.NLGrid[X,Y,1,2] = 2*self.Simulation.NLGrid[X,Y,1,1] - self.Simulation.NLGrid[X,Y,1,0] + pow(self.Simulation.Dt,2)*(pow(self.Simulation.MaterialProperties.WaveVelocityT,2)*((self.Simulation.NLGrid[X_,Y,1,1] - 2*self.Simulation.NLGrid[X,Y,1,1] + self.Simulation.NLGrid[_X,Y,1,1])/pow(self.Simulation.Dx,2)) + pow(self.Simulation.MaterialProperties.BetaT,1)*(((self.Simulation.Grid[X_,Y,1,1] - 2*self.Simulation.Grid[X,Y,1,1] + self.Simulation.Grid[_X,Y,1,1])*(self.Simulation.Grid[X_,Y,0,1] - self.Simulation.Grid[_X,Y,0,1])/(2*pow(self.Simulation.Dx,3))) + (self.Simulation.Grid[X_,Y,0,1] -2*self.Simulation.Grid[X,Y,0,1] + self.Simulation.Grid[_X,Y,0,1])*(self.Simulation.Grid[X_,Y,1,1] - self.Simulation.Grid[_X,Y,1,1])/(2*pow(self.Simulation.Dx,3))))
            
            
            self.Simulation.SourceSignal[i,0] = self.Simulation.NLGrid[5,15,0,2] #+ self.Simulation.NLGrid[5,15,0,2]
            
            #print self.Simulation.Grid[15,15,0,2]
           
             #Updates go Here
            self.Simulation.Grid[:,:,1,0] = self.Simulation.Grid[:,:,1,1]
            self.Simulation.Grid[:,:,1,1] =  self.Simulation.Grid[:,:,1,2]
            
            self.Simulation.Grid[:,:,0,0] = self.Simulation.Grid[:,:,0,1]
            self.Simulation.Grid[:,:,0,1] =  self.Simulation.Grid[:,:,0,2]
            
            self.Simulation.NLGrid[:,:,1,0] = self.Simulation.NLGrid[:,:,1,1]
            self.Simulation.NLGrid[:,:,1,1] =  self.Simulation.NLGrid[:,:,1,2]
            
            self.Simulation.NLGrid[:,:,0,0] = self.Simulation.NLGrid[:,:,0,1]
            self.Simulation.NLGrid[:,:,0,1] =  self.Simulation.NLGrid[:,:,0,2]
            #Updated
#            print i
            if i%10 == 0:
                self.putMovie(0.01)    
                pass
                #p.plot.show()
        print self.Simulation.MaterialProperties.BetaL, self.Simulation.MaterialProperties.BetaT, self.Simulation.MaterialProperties.WaveVelocityL, self.Simulation.Dt
        
        figure(2)
        plot(self.Simulation.SourceSignal)
        show()
                
    def __init__(self, Simulation = None):
        if Simulation is None:
            raise ValueError("Simulation Cannot be None. Please Initialize a New Simulation to proceed")
        else:
            self.Simulation = Simulation  
            self.Solve()

if __name__ == "__main__":
    raise Exception("Cannot run file as a standalone file. Please run through proper initialized channels")
