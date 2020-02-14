"""
Unit and regression test for the molpy package.
"""

# Import package, test suite, and other packages as needed
import molpy
import pytest
import sys


def test_molpy_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molpy" in sys.modules


def test_molecule_distance():

    mol = molpy.Molecule(["He", "He"], [[0, 0, 0], [0, 0, 1]])
    assert pytest.approx(1.0) == mol.distance(0, 1)

def test_name_molecule_distance():

    mol = molpy.NamedMolecule("Helium Dimer",["He", "He"], [[0, 0, 0], [0, 0, 1]])
    assert pytest.approx(1.0) == mol.distance(0, 1)