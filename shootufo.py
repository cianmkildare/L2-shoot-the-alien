import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "ufo shooting game"

message = ""

alien = Actor("ufo")

alien.pos = 50,50

def draw():
    screen.clear()
    screen.fill (color = (23, 19, 240))

    alien.draw()
    screen.draw.text(message,center = (250,50),fontsize = 30)

def placealien():
    alien.x = randint(10,490)
    alien.y = randint(10,490)

def on_mouse_down(pos):
    global message 
    if alien.collidepoint(pos):
        message = "good shot"
        placealien()

    else:
        message = "you missed"

placealien()




















pgzrun.go()