import typing
from collections.abc import Callable
from pgzero.actor import Actor

from boing.pos import Pos

WIDTH = 800
HEIGHT = 480
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6
class Ball(Actor):
    def __init__(self, dx):
        super().__init__("ball", (0,0))
        # remover isso e colocar em outro lugar
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

    def update(self):
        for i in range(self.speed):
            original_x = self.x
            self.x += self.dx
            self.y += self.dy
            new_dir_x = -1
            bat = self.bats[1]
            if abs(self.x - HALF_WIDTH) >= 344 and abs(original_x - HALF_WIDTH) < 344:
                if self.x < HALF_WIDTH:
                    new_dir_x = 1
                    bat = self.bats[0]
                    
            difference_y = self.y - bat.y
            
            if difference_y > -64 and difference_y < 64:
                self.dx = -self.dx
                self.dy += difference_y / 128
                self.dy = min(max(self.dy, -1), 1)
                self.dx, self.dy = normalised(self.dx, self.dy)
                game.impacts.append(Impact((self.x - new_dir_x * 10, self.y)))
                self.speed += 1
                self.ia_offset_changer()
                bat.timer = 10
                game.play_sound("hit", 5)
                if self.speed <= 10:
                    game.play_sound("hit_slow", 1)
                elif self.speed <= 12:
                    game.play_sound("hit_medium", 1)
                elif self.speed <= 16:
                    game.play_sound("hit_fast", 1)
                else:
                    game.play_sound("hit_veryfast", 1)
                    
            if abs(self.y - HALF_HEIGHT) > 220:
                self.dy = -self.dy
                self.y += self.dy
                game.impacts.append(Impact(self.pos))
                game.play_sound("bounce", 5)
                game.play_sound("bounce_synth", 1)
    def out(self):
        return self.x < 0 or self.x > WIDTH