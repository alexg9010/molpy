import numpy as np


def distance(point1, point2):
    """
    Calculate distance between two points.

    Parameters
    ----------
    point1 : array_like
        The first point.
    point2 : array_like
        The second point.

    Returns
    -------
    float
        The distance between point1 and point2.
    """
    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)


def read_xyz(filename):
    """
    Open an xyz file and return symbols and coordinates.

    Parameters
    ----------
    file_location : string
        File location of xyz file.

    Returns
    -------
    symbols
        The atomic symbols.
    coords
        Tho coordinates of the atoms.
    """
    xyz_file = np.genfromtxt(
        fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:, 0]
    coords = (xyz_file[:, 1:])
    coords = coords.astype(np.float)
    
    return {"symbols": symbols, "geometry" : coords}

# def read_xyz(filename):

#     with open(filename, "r") as handle:
#         data = handle.readlines()

#     data = data[2:]
#     data = [x.split() for x in data]
#     symbols = [x[0] for x in data]
#     xyz = np.array([[float(y) for y in x[1:]] for x in data])

#     return {"symbols": np.array(symbols), "geometry": xyz}
