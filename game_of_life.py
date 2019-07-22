# Author: Javier Roman

import sys
from utils import *
from grid import Grid
from p5 import *

pressed = False # Global variable that indicates if the spacebar has been pressed or not

def key_pressed():
    """
    This function overrides p5 key_pressed function. When the spacebar  
    is pressed the pressed flag is set to True meaning that the evolution of
    the population has to begin. If the spacebar is pressed another time the
    evolution is stopped.
    """
    global pressed
    if key  == ' ':
        pressed = not pressed

def mouse_pressed():
    """
    This function overrides p5 mouse_pressed function. When the user clicks a cell
    this cell becomes alive.
    """
    c, r = int(mouse_x*COLS/W), int(mouse_y*ROWS/H)
    grid.add((r,c))

def setup():
    """
    Setup for the sketch.
    """
    size(W, H)
    global grid
    grid = Grid(ROWS, COLS, 0)

def draw():
    """
    This function draws the environment and the cells.
    """
    background(255)
    grid.draw()
    if pressed:
        grid.generation()

if __name__ == '__main__':
    run()