import pgzero, pgzrun, pygame
import math, sys, random
from boing.state import State
from boing.game import Game

if sys.version_info < (3,5):
    print("This game requires at least version 3.5 of Python. Please download"
        "it from www.python.org")
    sys.exit()

pgzero_version = [int(s) if s.isnumeric() else s for s in pgzero.__version__.split('.')]

if pgzero_version < [1,2]:
    print("This game requires at least version 1.2 of Pygame Zero. You are"
            "using version {pgzero.__version__}. Please upgrade using the command"
            "'pip install --upgrade pgzero'")
    sys.exit()

WIDTH = 800
HEIGHT = 480
TITLE = "Boing!"
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6

num_players = 1
space_down = False

def normalised(x, y):
   length = math.hypot(x, y)
   return (x / length, y / length)

def sign(x):
   return -1 if x < 0 else 1

def p1_controls():
    move = 0
    if keyboard.z or keyboard.down:
        move = PLAYER_SPEED
    elif keyboard.a or keyboard.up:
        move = -PLAYER_SPEED
    return move

def p2_controls():
    move = 0
    if keyboard.m:
        move = PLAYER_SPEED
    elif keyboard.k:
        move = -PLAYER_SPEED
    return move

def update():
    global state, game, num_players, space_down
    space_pressed = False

    if keyboard.space and not space_down:
        space_pressed = True

    space_down = keyboard.space

    if state == State.MENU:
        if space_pressed:
            state = State.PLAY
            controls = [p1_controls]
            controls.append(p2_controls if num_players == 2 else None)

            game = Game(controls)
        else:
            if num_players == 2 and keyboard.up:
                sounds.up.play()
                num_players = 1
            elif num_players == 1 and keyboard.down:
                sounds.down.play()
                num_players = 2
            game.update()

    elif state == State.PLAY:
        if max(game.bats[0].score, game.bats[1].score) > 9:
            state = State.GAME_OVER
        else:
            game.update()

    elif state == State.GAME_OVER:
        if space_pressed:
            state = State.MENU
            num_players = 1
            game = Game()

def draw():
    game.draw()
    if state == State.MENU:
        menu_image = "menu" + str(num_players - 1)
        screen.blit(menu_image, (0,0))
    elif state == State.GAME_OVER:
        screen.blit("over", (0,0))

try:
   pygame.mixer.quit()
   pygame.mixer.init(44100, -16, 2, 1024)
   music.play("theme")
   music.set_volume(0.3)
except:
   pass

state = State.MENU
game = Game()
pgzrun.go()
