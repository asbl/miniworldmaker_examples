import random

from miniworldmaker import *


class MyBoard(PixelBoard):

    def on_setup(self):
        self.background.add_image("images/background.png")
        Bird((75, 200))
        self.pipe1 = Pipe(position=(260, self.height - 280))
        self.pipe2 = Pipe(position=(520, 0))
        self.pipe2.top()
        self.pipe3 = Pipe(position=(780, self.height - 280))
        self.pipe4 = Pipe(position=(760, -100))
        self.pipe4.top()
        self.score = NumberToken(position=(0, 0))
        self.score.size = (40, 40)
        #self.score.set_number(0)
        self.is_running = False

    def act(self):
        pass


class Bird(Token):

    def on_setup(self):
        self.add_image("images/fly.png")
        self.size = (60, 60)
        self.costume.orientation = 180
        self.flip_x()

    def setup_physics(self):
        self.physics.size = (0.8, 0.8)
        self.physics.shape_type = "circle"

    def on_sensing_borders(self, borders):
        if "bottom" in borders or "top" in borders:
            self.board.is_running = False

    def on_sensing_collision_with_pipe(self, other, info):
        self.board.is_running = False
        self.board.reset()

    def on_key_pressed(self, keys):
        if "SPACE" in keys:
            self.physics.velocity_y = 200
            if self.board.is_running is False:
                self.board.is_running = True


class Pipe(Token):

    def on_setup(self):
        self.add_image("images/pipe1.png")
        self.size = (80, 300)
        self.passed = False
        self.speed = 5

    def setup_physics(self):
        self.physics.gravity = False

    def top(self):
        self.costume.orientation = -180

    def act(self):
        self.move_in_direction("left")
        if self.position.x < 75 and self.passed is False:
            self.passed = True
            self.board.score.inc()

    def on_sensing_borders(self, borders):
        if "left" in borders:
            self.move_to(position=BoardPosition(self.position.x + random.randint(750, 800), self.y))
            self.passed = False


board = MyBoard(800, 600)
board.show()
