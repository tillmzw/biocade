import arcade
import pymunk
import random
import math


class Molecule(arcade.Sprite):
    def __init__(self, img, x, y, width, height):
        super().__init__(img, 1, 0, 0, 0, 0, x, y)
        self.width = width
        self.height = height
        self.pymunk_shape = self.create_physics()

    def create_physics(self):
        mass = random.randint(10, 10)
        moment = pymunk.moment_for_box(mass, (self.width, self.height))
        body = pymunk.Body(mass, moment)
        body.position = pymunk.Vec2d(self.center_x, self.center_y)
        body.velocity = random.randint(-200, 200), random.randint(-200, 200)
        shape = pymunk.Poly.create_box(body, (self.width, self.height))
        shape.friction = 1
        shape.elasticity = 1
        shape.arcada_sprite = self
        return shape

    def update(self):
        self.center_x = self.pymunk_shape.body.position.x
        self.center_y = self.pymunk_shape.body.position.y
        self.angle = math.degrees(self.pymunk_shape.body.angle)

    def on_hit(self):
        print('hello')
