import numpy as np
import scipy as sp
import defaults as df
from matplotlib.pyplot import imshow
class Solver:

    Simulation = None
    Location = None
    Width = None
    
    
    #Line Sources only, currently. Multiple Sources must be accounted for, Must think of a matrix solution. So much fight for something that might not even work. Pain.
    def setSource(self, Location = None, Width = None, Theta = None) :
        
        if Location is None:
            self.Location = [df.LOCATION/self.Simulation.Dx]
        else:
            self.Location.append(Location/self.Simulation.Dx)

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
        for i in range(1,int(r_var)):
            #Solving for Displacements in the X direction
            self.Simulation.Grid[X,Y,0,2] = 2*self.Simulation.Grid[X,Y,0,1] - self.Simulation.Grid[X,Y,0,0] + (pow(self.Simulation.Dt,2)/self.Simulation.MaterialProperties.Rho)*(
            
            (self.Simulation.MaterialProperties.Mu/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X_,Y,0,1] -2*self.Simulation.Grid[X,Y,0,1] + self.Simulation.Grid[_X,Y,0,1]) + ((self.Simulation.MaterialProperties.Mu/3 + self.Simulation.MaterialProperties.K)/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X_,Y,0,1] -2*self.Simulation.Grid[X,Y,0,1] + self.Simulation.Grid[_X,Y,0,1])
            )
            
            #Solving for Y
            
            self.Simulation.Grid[X,Y,1,2] = 2*self.Simulation.Grid[X,Y,1,1] - self.Simulation.Grid[X,Y,1,0] + (pow(self.Simulation.Dt,2)/self.Simulation.MaterialProperties.Rho)*(
            
            (self.Simulation.MaterialProperties.Mu/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X,_Y,1,1] -2*self.Simulation.Grid[X,Y,1,1] + self.Simulation.Grid[X,_Y,1,1]) + ((self.Simulation.MaterialProperties.Mu/3 + self.Simulation.MaterialProperties.K)/pow(self.Simulation.Dx,2))*(self.Simulation.Grid[X,Y_,1,1] -2*self.Simulation.Grid[X,Y,1,1] + self.Simulation.Grid[X,_Y,1,1])
            )
            
            #Updates go Here
            self.Simulation.Grid[:,:,1,0] = self.Simulation.Grid[:,:,1,1]
            self.Simulation.Grid[:,:,1,1] =  self.Simulation.Grid[:,:,1,2]
            
            self.Simulation.Grid[:,:,0,0] = self.Simulation.Grid[:,:,0,1]
            self.Simulation.Grid[:,:,0,1] =  self.Simulation.Grid[:,:,0,2]
            #Updated
            if i%3 == 0:
                imshow(np.reshape(self.Simulation.Grid[:,:,0,1], (self.Simulation.Dimensions[0],self.Simulation.Dimensions[0])))
                #p.plot.show()
        
    def __init__(self, Simulation = None):
        if Simulation is None:
            raise ValueError("Simulation Cannot be None. Please Initialize a New Simulation to proceed")
        else:
            self.Simulation = Simulation  
            self.Solve()

if __name__ == "__main__":
    raise Exception("Cannot run file as a standalone file. Please run through proper initialized channels")
