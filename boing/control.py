PLAYER_SPEED = 6

class Control:
    def __init__(self, up, down):
        self.up = up
        self.down = down
        
    def move(self):
        move = 0
        if self.down:
            move = PLAYER_SPEED
        elif self.up:
            move = -PLAYER_SPEED
        return move