class Solver:

    Simulation = None
    Location = None
    Width = None
    
    #Line Sources only, currently
    def setSource(self, Location = None, Width = None, Theta = None) :
        
        if Location is None:
            self.Location = df.LOCATION
        else:
            self.Location = Location
        
    
    def Solve(self):
        pass
        
    def __init__(self, Simulation = None):
        if Simulation is None:
            raise ValueError("Simulation Cannot be None. Please Initialize a New Simulation to proceed")
        else:
            self.Simulation = Simulation  
            self.Solve()

if __name__ == "__main__":
    raise Exception("Cannot run file as a standalone file. Please run through proper initialized channels")

