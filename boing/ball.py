from collections.abc import Callable

from pgzero.actor import Actor

from boing.pos import Pos
from boing.utils import normalised

WIDTH = 800
HEIGHT = 480
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6


class Ball(Actor):
    def __init__(self, dx):
        super().__init__("ball", (0, 0))
        self.hit_bat_callback = None
        self.hit_wall_callback = None
        self.x, self.y = HALF_WIDTH, HALF_HEIGHT
        self.dx, self.dy = dx, 0
        self.speed = 5
        self.bats = [Pos(), Pos()]
        self.ia_offset_changer = None

    def fist_bat_position_listener(self, pos: Pos) -> None:
        self.bats[0] = pos

    def second_bat_position_listener(self, pos: Pos) -> None:
        self.bats[1] = pos

    def ia_offset_listener(self, ia_offset_changer: Callable[[], None]) -> None:
        self.ia_offset_changer = ia_offset_changer

    def on_hit_bat(self, callback: Callable[[Pos, int], None]) -> None:
        self.hit_bat_callback = callback

    def hit_bat(self, pos: Pos, speed: int) -> None:
        if self.hit_bat_callback is not None:
            self.hit_bat_callback(pos, speed)

    def on_hit_wall(self, callback: Callable[[Pos], None]):
        self.hit_wall_callback = callback

    def hit_wall(self, pos: Pos) -> None:
        if self.hit_wall_callback is not None:
            self.hit_wall_callback(pos)

    def update(self):
        for i in range(self.speed):
            original_x = self.x
            self.x += self.dx
            self.y += self.dy
            new_dir_x = -1
            bat = self.bats[1]
            if abs(self.x - HALF_WIDTH) >= 344 > abs(original_x - HALF_WIDTH):
                if self.x < HALF_WIDTH:
                    new_dir_x = 1
                    bat = self.bats[0]

                difference_y = self.y - bat.y

                if -64 < difference_y < 64:
                    self.dx = -self.dx
                    self.dy += difference_y / 128
                    self.dy = min(max(self.dy, -1), 1)
                    self.dx, self.dy = normalised(self.dx, self.dy)
                    self.speed += 1
                    self.ia_offset_changer()

                    pos = Pos(self.x - new_dir_x * 10, self.y)
                    self.hit_bat(pos, self.speed)

            if abs(self.y - HALF_HEIGHT) > 220:
                self.dy = -self.dy
                self.y += self.dy
                self.hit_wall(self.pos)

    def out(self):
        return self.x < 0 or self.x > WIDTH
