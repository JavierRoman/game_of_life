import sys, time
from p5 import *
from random import randint

W, H = 500, 500
ROWS, COLS = 30, 30
pressed = False

class Grid:
    def __init__(self, rows, cols, p, offset=10):
        self.rows = rows
        self.cols = cols
        self.offset = offset
        self.live = set()
        self.__survivors = None
        self.create_grid(p)

    def add(self, position: tuple):
        self.live.add(position)

    def neighbours(self, pos, empty=False):
        i, j = pos
        neighbours = set()
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                neighbour = (i+di, j+dj)
                if neighbour==pos:
                    continue
                if empty:
                    if neighbour not in self.live:
                        neighbours.add(neighbour)
                else:
                    if neighbour in self.live:
                        neighbours.add(neighbour)
        
        return neighbours

    def cell_in_bounds(self, cell):
        r, c = cell
        return r < self.rows+self.offset and r >= -self.offset and c < self.cols+self.offset and c >= -self.offset

    def natural_selection(self, cell):
        living_cells = len(self.neighbours(cell))
        if cell in self.live:
            if living_cells < 2 or living_cells > 3:
                self.__survivors.remove(cell) # Dies (Underpopulation or Overpopulation)
        else:
            if living_cells == 3:
                if self.cell_in_bounds(cell):
                    self.__survivors.add(cell) # It becomes alive
            
    def generation(self):
        cells_to_check = self.live.copy()
        temp_set = set()
        for cell in cells_to_check:
            temp_set|=self.neighbours(cell, empty=True)
        cells_to_check|=temp_set
        cells_to_check = sorted(list(cells_to_check))
        self.__survivors = self.live.copy()
        for cell in cells_to_check:
            self.natural_selection(cell)
        self.live = self.__survivors.copy()

    def create_grid(self, p):
        for _ in range(int(self.rows*self.cols*p)):
            i, j = random2d(self.rows-1, self.cols-1)
            while (i, j) in self.live:
                i, j = random2d(self.rows-1, self.cols-1)
            self.add((i,j))

    def draw(self):
        sq_w, sq_h = W/float(self.cols), H/float(self.rows)
        for i, j in self.live:
            fill(0)
            x, y = j*sq_w, i*sq_h
            rect((x, y), sq_w, sq_h)

def range2d(i, j):
    return ((ii, jj) for ii in range(i) for jj in range(j))

def random2d(maxI, maxJ):
    i = randint(0, maxI)
    j = randint(0, maxJ)

    return i, j    

def key_pressed(event):
    global pressed
    if key  == ' ':
        pressed = not pressed

def mouse_pressed():
    c, r = int(mouse_x*COLS/W), int(mouse_y*ROWS/H)
    grid.add((r,c))

def setup():
    size(W, H)
    global grid
    grid = Grid(ROWS, COLS, 0)

def draw():
    background(255)
    grid.draw()
    if pressed:
        grid.generation()

if __name__ == '__main__':
    run()