# Author: Javier Roman

from utils import *
from p5 import *

class Grid:
    """
    This class implement every functionality needed to perform the simulations
    of the populations of cells based on the rules proposed for the Game Of Life.
    """
    def __init__(self, rows, cols, p, offset=5):
        """
        Constructor of the class.
        
        Args:
            rows (int): Number of rows of the grid.
            cols (int): Number of columns of the grid.
            p (float): Percentage of cells alive.
            offset (int, optional): Cells outside the canvas that are still simulated. Defaults to 5.
        """
        self.rows = rows
        self.cols = cols
        self.offset = offset
        self.live = set()
        self.__survivors = None
        self.create_grid(p)

    def add(self, position: tuple):
        """
        This method adds a cell to the set of alive cells.
        
        Args:
            position (tuple): Pair of values representing a 2d spatial position in the grid.
        """
        self.live.add(position)

    def neighbours(self, pos, empty=False):
        """
        This method returns the set of neighbours of one certain cell.
        
        Args:
            pos (tuple): 2d spatial position of a cell.
            empty (bool, optional): When specified only dead neighbours cells are retrieved. Defaults to False.
        
        Returns:
            list: List of cell positions.
        """ 
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
        """
        Checks if a certain cell being simulated is in-bounds including the offset.
        
        Args:
            cell (tuple): 2d spatial position of the cell.
        
        Returns:
            bool: True if the cell is in-bounds False otherwise.
        """
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
        """
        This function simulates one generation in a very efficient way. Instead of looking
        for every cell in the grid it only looks for the cells alive and the dead neighbours
        of those cells.
        """
        cells_to_check = self.live.copy()
        temp_set = set()
        for cell in cells_to_check:
            temp_set|=self.neighbours(cell, empty=True)
        cells_to_check|=temp_set
        self.__survivors = self.live.copy()
        for cell in cells_to_check:
            self.natural_selection(cell)
        self.live = self.__survivors.copy()

    def create_grid(self, p):
        """
        This function creates the whole grid with p*rows*cols alive cells.
        
        Args:
            p (float): Percentage of cells alive.
        """
        for _ in range(int(self.rows*self.cols*p)):
            i, j = random2d(self.rows-1, self.cols-1)
            while (i, j) in self.live:
                i, j = random2d(self.rows-1, self.cols-1)
            self.add((i,j))

    def draw(self):
        """
        This function draws the alive cells in their corresponding position.
        """
        sq_w, sq_h = W/float(self.cols), H/float(self.rows)
        for i, j in self.live:
            fill(0)
            x, y = j*sq_w, i*sq_h
            rect((x, y), sq_w, sq_h)