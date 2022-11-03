import typing

from boing.control import Control
from boing.pos import Pos

WIDTH = 800
HEIGHT = 480
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
MAX_AI_SPEED = 6


class AIControl(Control):
    def __init__(self, ai_offset):
        super().__init__(None, None)
        self.ball = Pos()
        self.ai_offset = ai_offset
        self.x = 0
        self.y = 0

    def my_bat_position_listener(self, pos: Pos) -> None:
        self.x = pos.x
        self.y = pos.y

    def ball_position_listener(self, pos: Pos) -> None:
        self.ball = pos

    def move(self):  # Mover para uma classe própria
        x_distance = abs(self.ball.x - self.x)
        target_y_1 = HALF_HEIGHT
        target_y_2 = self.ball.y + self.ai_offset
        weight1 = min(1, x_distance / HALF_WIDTH)
        weight2 = 1 - weight1
        target_y = (weight1 * target_y_1) + (weight2 * target_y_2)
        return min(MAX_AI_SPEED, max(-MAX_AI_SPEED, target_y - self.y))
