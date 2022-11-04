from pgzero.keyboard import Keyboard

from boing.constants import PLAYER_SPEED


class Control:
    def __init__(self, keyboard: Keyboard, up, down):
        self.keyboard = keyboard
        self.up = up
        self.down = down

    def move(self):
        move = 0
        if getattr(self.keyboard, self.down):
            move = -PLAYER_SPEED
        elif getattr(self.keyboard, self.up):
            move = PLAYER_SPEED
        return move
