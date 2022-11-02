import pgzrun

import math
import pygame

from boing.game import Game
from boing.state import State

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
    return x / length, y / length


def sign(x):
    return -1 if x < 0 else 1


def update():
    global state, game, num_players, space_down
    space_pressed = False

    if keyboard.space and not space_down:
        space_pressed = True

    space_down = keyboard.space

    if state == State.MENU:
        game = Game(screen)
        if space_pressed:
            state = State.PLAY
            game = Game(screen, num_players)
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
            game = Game(screen)


def draw():
    game.draw()
    if state == State.MENU:
        menu_image = "menu" + str(num_players - 1)
        screen.blit(menu_image, (0, 0))
    elif state == State.GAME_OVER:
        screen.blit("over", (0, 0))


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
