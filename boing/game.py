from pgzero import keyboard
from pgzero.keyboard import Keyboard

from boing.ball import Ball
from boing.bat import Bat
from boing.control import Control
from boing.ai_control import AIControl

WIDTH = 800
HEIGHT = 480
TITLE = "Boing!"
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6

class Game:
    def __init__(self, controls = 0):
        self.first_bat_position_listener = []
        self.second_bat_position_listener = []
        self.ball_position_listener = []
        self.ball = Ball(-1)
        ball.ia_offset_listener(self.ia_offsets_randomize)
        self.first_bat_position_listener.append(self.ball.fist_bat_position_listener)
        self.second_bat_position_listener.append(self.ball.second_bat_position_listener)
        self.ai_offsets = 0
        self.bats = []


        if controls > 0:
            self.bats.append(Bat(0, Control(keyboard.z,  keyboard.a)))
        else:
            ai1 =AIControl(self.ai_offsets)
            self.first_bat_position_listener.append(ai1.my_bat_position_listener)
            self.ball_position_listener.append(ai1.ball_position_listener)
            self.bats.append(Bat(0, ai1))
        if controls > 1:
            self.bats.append(Bat(1, Control(keyboard.m, keyboard.k)))
        else:
            ai2 = AIControl(self.ai_offsets)
            self.second_bat_position_listener.append(ai2.my_bat_position_listener)
            self.ball_position_listener.append(ai2.ball_position_listener)
            self.bats.append(Bat(1, ai2))
        self.impacts = []

    def ia_offsets_randomize(self):
        self.ai_offsets = random.randint(-10, 10)
    def update(self):
        for obj in self.bats + [self.ball] + self.impacts:
            obj.update()

        for listener in self.first_bat_position_listener:
            listener(Pos(self.bats[0].x, self.bats[0].y))

        for listener in self.second_bat_position_listener:
            listener(Pos(self.bats[1].x, self.bats[1].y))

        for listener in self.ball_position_listener:
            listener(Pos(self.ball.x, self.ball.y))

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