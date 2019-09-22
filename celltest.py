from ising_class import *

acell= cell(3,3,10)  #Args: i, j, n
print(acell.cellspin())

acell.spin.flip()  # reaching through cell to inner spin object
print(acell.left)  # directly accesing the left neighbor indices
print(acell.right)  # accesing the rigth neighbor indices
print(acell.up)   # accessing the up neighbor indices
print(acell.down)   # accessign the down neighbor indices
