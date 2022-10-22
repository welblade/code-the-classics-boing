import math, random
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 480
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6

class Bat(Actor):
    def __init__(self, player, move_func=None):
        # colocar em player posição na tela
        x = 40 if player == 0 else 760 
        # de onde essa variável deveria vir?
        y = HALF_HEIGHT 
        
        super().__init__("blank", (x, y))
        self.player = player 
        self.score = 0
        
        if move_func != None:
            self.move_func = move_func # Função de movimento, melhor criar uma outra classe para CPU
        else:
            self.move_func = self.ai
            self.timer = 0
    
    def setPosition(x, y):
        self.x = x 
        self.y = y
        
    def update(self):
        self.timer -= 1
        y_movement = self.move_func()
        self.y = min(400, max(80, self.y + y_movement))
        frame = 0
        if self.timer > 0:
            if game.ball.out():
                frame = 2
            else:
                frame = 1
        self.image = "bat" + str(self.player) + str(frame)
        
    def ai(self): #Mover para uma classe própria
        x_distance = abs(game.ball.x - self.x)
        target_y_1 = HALF_HEIGHT
        target_y_2 = game.ball.y + game.ai_offset
        weight1 = min(1, x_distance / HALF_WIDTH)
        weight2 = 1 - weight1
        target_y = (weight1 * target_y_1) + (weight2 * target_y_2)