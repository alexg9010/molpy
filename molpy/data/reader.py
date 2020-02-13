import os

# from ..util import read_xyz     ## python3 way
# from molpy import util          ## import whole util, not recommmende
# python2 way, independent of relative file location
from molpy.util import read_xyz

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')

with open(filename, 'r') as handle:
    look_and_say = handle.read()


def get_molecule(molecule):
    """Call read_xyz for molecule.

    Extract symbols and geometry for given molecule from data folder.

    Parameters
    ----------
    molecule : string
        prefix of the .xyz file

    Returns
    -------
    molecule : `dict`
        This output is described in :func:`~molpy.util.read_xyz`
    """
    return read_xyz(os.path.join(dirname, molecule + ".xyz"))
