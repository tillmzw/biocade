import arcade


class Protein(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./ressources/image/Apoptosome.png")
        self.center_x = x
        self.center_y = y
        self.width = 20
        self.height = 20

    def move(self):
        self.center_y += 1
