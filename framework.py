from formulation import simulation
from solver import Solver as sl

#Limit of L and M in terms of percentages. How do we combine this? We need to run experiments, check correlations and all. Let's see if it has any effect:w

__LIMIT = 10

for percent in range(-int(round(__LIMIT)), int(round(__LIMIT))+1):
    sim = simulation()
    oldl = sim.getParam('l')
    print percent/100.0
    newl = oldl*(1 + (percent/100.0))
    print oldl, newl
    sim.setParam('l', newl)
    sim.setMixing(True)
    sl(sim)
    sim.save("Simulation_Save_l_%d_percent.mat"%percent)

for percent in range(-int(round(__LIMIT)), int(round(__LIMIT))+1):
    sim = simulation()
    oldl = sim.getParam('m')
    print percent/100.0
    newl = oldl*(1 + (percent/100.0))
    print oldl, newl
    sim.setParam('m', newl)
    sim.setMixing(True)
    sl(sim)
    sim.save("Simulation_Save_m_%d_percent.mat"%percent)
