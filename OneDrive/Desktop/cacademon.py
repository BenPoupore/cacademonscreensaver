import pygame as pg
from pynput import keyboard
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

pg.init()
pg.display.init
screen = pg.display.set_mode((width,height))
clock = pg.time.Clock()

pog = pg.image.load("pog.png")
pog = pg.transform.scale(pog, (100, 100))

pogleft = pg.image.load("pog.png")
pogleft = pg.transform.scale(pogleft, (100, 100))
pogleft = pg.transform.flip(pogleft, True, False)

AHHH = pg.image.load("lookat.png")
AHHH = pg.transform.scale(AHHH, (100, 100))

x = 0
y = 0

directionx = 1
directiony = 1

while True:

    clock.tick(144)
    screen.fill((10,10,10))

    mx,my = pg.mouse.get_pos()

    if (x+100 > width):
        directionx = -1
    if (x < 0):
        directionx = 1

    if (y+100 > height):
        directiony = -1
    if (y < 0):
        directiony = 1
         
    x=x+directionx
    y=y+directiony

    if (((mx>x) and (mx<x+100)) and (((my>y) and (my<y+100)))):
        screen.blit(AHHH,(x,y))
    if  not(((mx>x) and (mx<x+100)) and (((my>y) and (my<y+100)))):
        if(directionx>0):    
            screen.blit(pog,(x,y))
        if(directionx<0):    
            screen.blit(pogleft,(x,y))

    #print(clock)
    for event in pg.event.get():
        if event.type == pg.QUIT:
                exit()
    pg.display.update()
