from pgzero.actor import Actor
from boing.pos import Pos

WIDTH = 800
HEIGHT = 480
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6


class Bat(Actor):
    def __init__(self, player, control):
        x = 40 if player == 0 else 760
        y = HALF_HEIGHT
        super().__init__("blank", (x, y))
        self.is_ball_out = False;

        self.player = player
        self.score = 0

        self.timer = 0
        self.move_func = control.move
        self.image = "bat" + str(self.player) + "0"

    def ball_position_listener(self, pos: Pos):
        self.is_ball_out = pos.x < 0 or pos.x > WIDTH

    def update(self):
        self.timer -= 1
        y_movement = self.move_func()
        self.y = min(400, max(80, self.y + y_movement))
        frame = 0
        if self.timer > 0:
            if self.is_ball_out:
                frame = 2
            else:
                frame = 1
        self.image = "bat" + str(self.player) + str(frame)
