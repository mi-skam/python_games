import math
import pygame
import random
import tkinter as tkinter

from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dir_nx=1, dir_ny=0, color=(255, 0, 0)):
        pass

    def move(self, dir_nx, dir_ny):
        pass

    def draw(self, surface, eyes=False):
        pass

class Snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass

def draw_grid(w, rows, surface):
    size_between = w // rows
    
    x = 0
    y = 0
    for l in range(rows):
        x += size_between
        y += size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    global rows, width, height

    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()

def random_snack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, height, rows
    width = 500
    rows = 20

    win = pygame.display.set_mode((width, height))
    s = Snake(color=(255, 0, 0), pos=(10, 10))

    clock = pygame.time.Clock() # referrence time for frames

    while True:
        pygame.time.delay(50)
        clock.tick(10)

        redraw_window(surface=win)

rows = 20 
width = 800
height = 600

Cube.rows = rows
Cube.w = width

main()
