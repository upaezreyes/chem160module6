from ising_class import *
Temp = 2.3   # Temp.
n = 20   # sites per edge for nxn system
ntrials = 500000  # number trials
nequil = 100000  # Equilibration steps

# initialize the system and temperature
ising1 = ising(Temp,n)
ising1.randomize()


while Temp<4.:
    ising1.changeTemp(Temp)
    # run 500000 trials of equilibration and clear properties
    ising1.trials(nequil)  # run equilibration steps
    ising1.resetprops()  # reset properties to make your, it start at zero

    for i in range(ntrials):
        ising1.trial()   # runs a single trial
        ising1.addprops()  # updates properties

    #calculate properties and print the final system
    ising1.calcprops()
    Temp += 0.2
ising1.printsys()
