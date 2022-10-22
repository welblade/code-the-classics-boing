from pgzero.actor import Actor

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
    
    def setPosition(x, y):
        self.x = x 
        self.y = y
    
    def update(self):
        for i in range(self.speed):
            original_x = self.x
            self.x += self.dx
            self.y += self.dy
            if abs(self.x - HALF_WIDTH) >= 344 and abs(original_x - HALF_WIDTH) < 344:
                if self.x < HALF_WIDTH:
                    new_dir_x = 1
                    bat = game.bats[0]
                else:
                    new_dir_x = -1
                    bat = game.bats[1]
                    
            difference_y = self.y - bat.y
            
            if difference_y > -64 and difference_y < 64:
                self.dx = -self.dx
                self.dy += difference_y / 128
                self.dy = min(max(self.dy, -1), 1)
                self.dx, self.dy = normalised(self.dx, self.dy)
                game.impacts.append(Impact((self.x - new_dir_x * 10, self.y)))
                self.speed += 1
                game.ai_offset = random.randint(-10, 10)
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