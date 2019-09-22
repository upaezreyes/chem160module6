from ising_class import *
aspin = spin()  # creates the spin object
print(aspin.char())    # print the character
print(aspin.myspin())  # print the value 

aspin.randomize()   # to randomize 
print(aspin.char())  # print out again

aspin.flip()   # to flip 
print(aspin.char())  # to print out again
