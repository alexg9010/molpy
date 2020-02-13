import pytest
import molpy
import numpy as np


@pytest.mark.parametrize("point1, point2, bench", [
    ([0, 1], [0, 0], 1),
    ([0, 2], [0, 0], 2),
    ([0, 3], [0, 0], 3),
    ([2.236, 2.236], [0, 0], 3.162),
])
def test_distance(point1, point2, bench):
    assert molpy.util.distance(point1, point2) == pytest.approx(bench, abs=1.e-3)


def test_distance_failure():
    assert molpy.util.distance([0], [3]) != 5


@pytest.mark.parametrize(
    "molecule, com, natoms",
    [("water", [9.81833333, 7.60366667, 12.673], 3), ("benzene", [-1.4045, 0, 0], 12)],
)
def test_read_xyz(molecule, com, natoms):

    mol = molpy.data.get_molecule(molecule)
    print(np.mean(mol["geometry"], axis=0))
    print(com)
    assert np.allclose(np.mean(mol["geometry"], axis=0), com)
    assert len(mol["geometry"]) == natoms
    assert len(mol["symbols"]) == natoms


def test_get_molecule():

    with pytest.raises(FileNotFoundError):
        # with pytest.raises(FileNotFoundError):
        mol = molpy.data.get_molecule("non-existant")
