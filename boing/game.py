from boing.bat import Bat
from boing.ball import Ball

WIDTH = 800
HEIGHT = 480
TITLE = "Boing!"
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6

class Game:
    def __init__(self, controls=(None, None)):
      self.bats = [Bat(0, controls[0]), Bat(1, controls[1])]
      self.ball = Ball(-1)
      self.impacts = []
      self.ai_offset = 0
      
    def update(self):
        for obj in self.bats + [self.ball] + self.impacts:
            obj.update()
            
        for i in range(len(self.impacts) - 1, -1, -1):
            if self.impacts[i].time >= 10:
                del self.impacts[i]
                
        if self.ball.out():
            scoring_player = 1 if self.ball.x < WIDTH // 2 else 0
            losing_player = 1 - scoring_player
            
        if self.bats[losing_player].timer < 0:
            self.bats[scoring_player].score += 1
            game.play_sound("score_goal", 1)
            self.bats[losing_player].timer = 20
            
        elif self.bats[losing_player].timer == 0:               
            direction = -1 if losing_player == 0 else 1
            self.ball = Ball(direction)
    
    def draw(self):
        screen.blit("table", (0,0))
        for p in (0,1):
            if self.bats[p].timer > 0 and game.ball.out():
                screen.blit("effect" + str(p), (0,0))
                
        for obj in self.bats + [self.ball] + self.impacts:
            obj.draw()
            
        for p in (0,1):
            score = "{0:02d}".format(self.bats[p].score)
            for i in (0,1):
                colour = "0"
                other_p = 1 - p
                
        if self.bats[other_p].timer > 0 and game.ball.out():
            colour = "2" if p == 0  else "1"
            
        image = "digit" + colour + str(score[i])
        screen.blit(image, (255 + (160 * p) + (i * 55), 46))
    
    def play_sound(self, name, count=1):
        if self.bats[0].move_func != self.bats[0].ai:
            try:
                getattr(sounds, name + str(random.randint(0, count - 1))).play()
            except:
                pass