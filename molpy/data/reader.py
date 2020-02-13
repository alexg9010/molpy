import os

# from ..util import read_xyz     ## python3 way
# from molpy import util          ## import whole util, not recommmende
from molpy.util import read_xyz  ## python2 way, independent of relative file location

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')

with open(filename, 'r') as handle:
    look_and_say = handle.read()


def get_molecule(filename):
    return read_xyz(os.path.join(dirname, filename + ".xyz"))
