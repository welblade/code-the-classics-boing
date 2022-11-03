import random

from pgzero.keyboard import Keyboard
from boing.ai_control import AIControl
from boing.ball import Ball
from boing.bat import Bat
from boing.control import Control
from boing.pos import Pos
from boing.sound import SoundPlayer
from boing.impact import Impact


WIDTH = 800
HEIGHT = 480
TITLE = "Boing!"
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6


class Game:
    def __init__(self, screen=None, sounds: SoundPlayer = None, keyboard: Keyboard = None, controls=0):
        self.screen = screen
        self.sounds = sounds
        self.first_bat_position_listener = []
        self.second_bat_position_listener = []
        self.ball_position_listener = []
        self.ball = self.new_ball(-1)
        self.ai_offsets = 0
        self.bats = []
        if controls > 0:
            control_1 = Control(keyboard, 'z', 'a')
        else:
            control_1 = AIControl(self.ai_offsets)
            self.first_bat_position_listener.append(control_1.my_bat_position_listener)
            self.ball_position_listener.append(control_1.ball_position_listener)

        player1 = Bat(0, control_1)
        self.ball_position_listener.append(player1.ball_position_listener)
        self.bats.append(player1)

        if controls > 1:
            control_2 = Control(keyboard, 'k', 'm')
        else:
            control_2 = AIControl(self.ai_offsets)
            self.second_bat_position_listener.append(control_2.my_bat_position_listener)
            self.ball_position_listener.append(control_2.ball_position_listener)

        player2 = Bat(1, control_2)
        self.ball_position_listener.append(player2.ball_position_listener)
        self.bats.append(player2)
        self.impacts = []

    def ia_offsets_randomize(self):
        self.ai_offsets = random.randint(-10, 10)

    def ball_hit_bat(self, pos: Pos, speed):
        self.impacts.append(Impact((pos.x, pos.y)))
        self.sounds.hit(speed)
        player = 0 if pos.x < HALF_WIDTH else 1
        self.bats[player].timer = 10

    def ball_hit_wall(self, pos: Pos):
        self.impacts.append(Impact((pos.x, pos.y)))
        self.sounds.bounce()

    def update(self):
        for listener in self.first_bat_position_listener:
            listener(Pos(self.bats[0].x, self.bats[0].y))

        for listener in self.second_bat_position_listener:
            listener(Pos(self.bats[1].x, self.bats[1].y))

        for listener in self.ball_position_listener:
            listener(Pos(self.ball.x, self.ball.y))

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
                self.bats[losing_player].timer = 20
                self.sounds.score_goal()
            elif self.bats[losing_player].timer == 0:
                direction = -1 if losing_player == 0 else 1
                self.ball = self.new_ball(direction)

    def draw(self):
        self.screen.blit("table", (0, 0))
        for p in (0, 1):
            if self.bats[p].timer > 0 and self.ball.out():
                self.screen.blit("effect" + str(p), (0, 0))

        for obj in self.bats + [self.ball] + self.impacts:
            obj.draw()

        for p in (0, 1):
            score = "{0:02d}".format(self.bats[p].score)
            for i in (0, 1):
                colour = "0"
                other_p = 1 - p

                if self.bats[other_p].timer > 0 and self.ball.out():
                    colour = "2" if p == 0 else "1"

                image = "digit" + colour + str(score[i])
                self.screen.blit(image, (255 + (160 * p) + (i * 55), 46))

    def new_ball(self, direction) -> Ball:
        ball = Ball(direction)
        ball.ia_offset_listener(self.ia_offsets_randomize)
        ball.on_hit_bat(self.ball_hit_bat)
        self.first_bat_position_listener.insert(0, ball.fist_bat_position_listener)
        self.second_bat_position_listener.insert(0, ball.second_bat_position_listener)
        return ball
