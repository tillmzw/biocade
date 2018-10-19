from molecule.molecule import Molecule


class Enzyme(Molecule):
    def __init__(self, x, y):
        super().__init__("./ressources/image/radenzyme.png", x, y, 30, 30)
