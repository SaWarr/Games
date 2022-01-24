# Another in more OO style

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# Cube object
class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, colour=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw (self, surfcae, eyes=False):
        pass

# Snake object
class snake(object):
    def __init__(self, colour, pos):
        pass

    def move(self):
        pass

    def reset(self,pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBetween = w // rows
    x = 0
    y = 0
    for l in range (rows):
        x = x + sizeBetween
        y = y + sizeBetween
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) 


def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass

def message_box(subject, contet):
    pass

def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (0,0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50) # Experiment with for difficulty
        clock.tick(10) # Experiment with for difficulty

        redrawWindow(win)
    
#rows =
#w =
#h =

#cube.rows = rows
#cube.w = w

main()

