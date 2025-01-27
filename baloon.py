import pgzrun
import os
from random import randint

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

WIDTH = 800
HEIGHT = 600

# actors
baloon = Actor("balloon")
baloon.x, baloon.y = 400, 300

bird = Actor("bird-up")
bird.x, bird.y = 1000, randint(0, 200)


# globals
up = False
game_over = False
bird_up = True
number_of_updates = 0

def draw():
    if not game_over:
        screen.blit("background", (0, 0))
        baloon.draw()
        bird.draw()
    else:
        screen.blit("background", (0, 0))
        screen.draw.text("Game over!", center=(400, 300), color="white", fontsize=60)

def on_mouse_down():
    global up
    up = True

def on_mouse_up():
    global up
    up = False

def update():
    global baloon, up, bird, game_over, bird_up, number_of_updates
    if not game_over:
        if up:
            baloon.y -= 3
        else:
            baloon.y += 3
        
        bird.x -= 3

        if bird.x == -50:
            bird.x = 1000
            bird.y = randint(0, 200)

        if number_of_updates == 20:
            if bird_up:
                bird.image = "bird-down"
                bird_up = False
            else:
                bird.image = "bird-up"
                bird_up = True
            number_of_updates = 0
        else:
            number_of_updates += 1

        if baloon.colliderect(bird):
            game_over = True


pgzrun.go()