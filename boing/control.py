from pgzero import keyboard
from pgzero.keyboard import Keyboard

class Control():
    def __init__(self):
        self.up = []
        self.down =[]
        
    def move(self):
        move = 0
        if keyboard.z or keyboard.down:
            move = PLAYER_SPEED
        elif keyboard.a or keyboard.up:
            move = -PLAYER_SPEED
        return move