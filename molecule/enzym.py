import arcade

class Enzym(arcade.sprite):
    def __init__(self, x, y):
        super().__init__("./ressources/image/radenzyme.png")
        self.center_x = x
        self.center_y = y
        self.width = 20
        self.height = 20