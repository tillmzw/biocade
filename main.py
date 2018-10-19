"""
This simple animation example shows how to use classes to animate
multiple objects on the screen at the same time.

Because this is redraws the shapes from scratch each frame, this is SLOW
and inefficient.

Using buffered drawing commands (Vertex Buffer Objects) is a bit more complex,
but faster.

See http://arcade.academy/examples/index.html#shape-lists for some examples.

Also, any Sprite class put in a SpriteList and drawn with the SpriteList will
be drawn using Vertex Buffer Objects for better performance.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.shapes
"""

import os
import math
import arcade
import pymunk
import random

# Set up the constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

RECT_WIDTH = 50
RECT_HEIGHT = 50

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class PSprite(arcade.Sprite):
    def __init__(self, pymunk_shape, filename):
        super().__init__(filename, center_x=pymunk_shape.body.position.x, center_y=pymunk_shape.body.position.y)
        self.pymunk_shape = pymunk_shape


class CircleSprite(PSprite):
    def __init__(self, pymunk_shape, filename):
        super().__init__(pymunk_shape, filename)
        self.width = pymunk_shape.radius * 2
        self.height = pymunk_shape.radius * 2


class BoxSprite(PSprite):
    def __init__(self, pymunk_shape, width, height):
        super().__init__(pymunk_shape, filename=os.path.join(BASE_PATH, "ressources/image/Apoptosome.png"))
        self.width = width
        self.height = height


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Shapes!")
        self.shape_list = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0)
        self.space.add_default_collision_handler()
        self.sprite_list = arcade.SpriteList()
        self.static_lines = []
        self.draw_time = 0
        self.processing_time = 0

        floor_height = 0
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        for x in (
                ((0, 0), (SCREEN_WIDTH, 0)),
                ((SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT)),
                ((SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)),
                ((0, SCREEN_HEIGHT), (0, 0))
                ):
            border_shape = pymunk.Segment(body, x[0], x[1], 0.0)
            border_shape.friction = 0
            self.space.add(border_shape)
            self.static_lines.append(border_shape)

        self.shape_list = []

        for i in range(50):

            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            width = random.randrange(50, 80)
            height = random.randrange(50, 80)

            size = random.randint(40, 40)
            mass = random.randint(10, 10)
            moment = pymunk.moment_for_box(mass, (size, size))
            body = pymunk.Body(mass, moment)
            body.position = pymunk.Vec2d(x, y)
            body.velocity = random.randint(-200, 200), random.randint(-200, 200)
            shape = pymunk.Poly.create_box(body, (size, size))
            shape.friction = 0
            self.space.add(body, shape)
            sprite = BoxSprite(shape, width=size, height=size)
            self.sprite_list.append(sprite)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        self.sprite_list.draw()
        for line in self.static_lines:
            body = line.body

            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            arcade.draw_line(pv1.x, pv1.y, pv2.x, pv2.y, arcade.color.WHITE, 2)

    def update(self, delta_time):
        self.space.step(1/60.0)

        for sprite in self.sprite_list:
            sprite.center_x = sprite.pymunk_shape.body.position.x
            sprite.center_y = sprite.pymunk_shape.body.position.y
            sprite.angle = math.degrees(sprite.pymunk_shape.body.angle)

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
