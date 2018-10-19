
from molecule.molecule import Molecule


class Protein(Molecule):
    def __init__(self, x, y):
        super().__init__("./ressources/image/Apoptosome.png", x, y, 20, 20)
