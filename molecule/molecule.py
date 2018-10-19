from random import random

import arcade
import pymunk


class Molecule(arcade.Sprite):
    def __init__(self, img, x, y, width, height):
        super().__init__(img, 1, 0, 0, 0, 0, x, y)
        self.width = width
        self.height = height
        self.pymunk_shape = self.create_physics()

    def create_physics(self):
        size = random.randint(40, 40)
        mass = random.randint(10, 10)
        moment = pymunk.moment_for_box(mass, (size, size))
        body = pymunk.Body(mass, moment)
        body.position = pymunk.Vec2d(self.center_x, self.center_y)
        body.velocity = random.randint(-200, 200), random.randint(-200, 200)
        shape = pymunk.Poly.create_box(body, (size, size))
        shape.friction = 0
        return shape

    def update(self):
        self.center_x = self.pymunk_shape.body.position.x
        self.center_y = self.pymunk_shape.body.position.y
