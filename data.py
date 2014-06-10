import defaults as df
from math import sqrt


## These classes are created to create a default set of elements. I will implement a file reader to get elelment data later. createing a new object of this type ensures that we get a nice default simulation. Let's hope this works. Solver is yet to be implemented. Sigh

class waveProperties:
    def __init__(self, Frequency = None):
        if Frequency is None:
            self.Frequency = df.FREQUENCY
        else:
            self.Frequency = Frequency
        
        self.WaveLength = None


class materialProperties:
    def __init__(self, Mu = None, K = None, Rho = None,  A = None, B = None, C = None,l = None, m = None, Lambda = None):
        
        ##Initialize All defaults if none.
        
        if Mu is None:
            self.Mu = df.MU
        else:
            self.Mu = Mu
                        
        if K is None:
            self.K = df.K
        else:
            self.K = K
            
        if Rho is None:
            self.Rho = df.RHO
        else:
            self.Rho = Rho
        
        if A is None:
            self.A = df.A
        else:
            self.A = A
        
        if B is None:
            self.B = df.B
        else:
            self.B = B
            
        if C is None:
            self.C = df.C
        else:
            self.C = C
       
        if l is None:
            self.l = df.l
        else:
            self.l = l

        if m is None:
            self.m = df.m
        else:
            self.m = m
        
        if Lambda is None:
            self.Lambda = df.Lambda
        else:
            self.Lambda = Lambda 
        
        self.WaveVelocityL = sqrt((self.Lambda + (2*self.Mu))/self.Rho)
        self.WaveVelocityT = sqrt(self.Mu/self.Rho)
        self.BetaL = 3 + 2*(self.l + 2*self.m)/(self.Lambda + 2*self.Mu)
        self.BetaT = (self.Lambda + 2*self.Mu)/self.Mu + self.m/self.Mu
            
class waveGuide:

    def __init__(self, Boundary = None):
        if Boundary is None:
            self.Boundary = df.BOUNDARY
        else:
            self.Boundary = Boundary

## Boundary Legend
## 0 - All reflecting
## 1 - Sides Reflecting Ends PML
## 2 - Sides PML Ends Reflecting
## 3 - Everything PML
