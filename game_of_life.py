# Author: Javier Roman

import sys
from argparse import ArgumentParser
from utils import *
from grid import Grid
from p5 import *

pressed = False # Global variable that indicates if the spacebar has been pressed or not
rows, cols = 30, 30 # Number of rows and columns of the grid.
population = 0.2  # Percentage of the cells alive

def parse_args():
    """
    This function parses execution arguments and return them.
    
    Raises:
        MazeSolverArgumentsException: This exception is raised when a conflict is found between arguments.
    
    Returns:
        class: Class with the different arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("-p", "--percentage", help="Percentage of cells alive.", 
                type=restricted_float, default=0.2, metavar="[0.0, 1.0]")
    parser.add_argument("-s", "--size", help="Size of the squared grid. Warning: With very big sizes the performance can be slow.", 
                type=int, default=30, metavar="SIZE")
    try:
        args = parser.parse_args()
    except:
        print("-h/--help for more information.")
        sys.exit(1)
    else:
        return args

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
    c, r = int(mouse_x*cols/W), int(mouse_y*rows/H)
    grid.add((r,c))

def setup():
    """
    Setup for the sketch.
    """
    size(W, H)
    global grid
    grid = Grid(rows, cols, population)

def draw():
    """
    This function draws the environment and the cells.
    """
    background(255)
    grid.draw()
    if pressed:
        grid.generation()

def main():
    global rows, cols, population
    args = parse_args()
    rows, cols = args.size, args.size
    population = args.percentage
    run()

if __name__ == '__main__':
    main()