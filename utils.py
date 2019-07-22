# Author: Javier Roman

from random import randint

# Some global variables
W, H = 500, 500 # Width and height of the canvas.
ROWS, COLS = 30, 30 # Number of rows and columns of the grid.

def range2d(i, j):
    """
    This function generates pairs of values from (0,0) to (i, j)
    
    Args:
        i (int): First value limit
        j (int): Second value limit
    
    Returns:
        tuple: Tuple of values in the range [ (0,0), (i, j) )
    """
    return ((ii, jj) for ii in range(i) for jj in range(j))

def random2d(maxI, maxJ):
    """
    This function generates a random pair if integers between (0, 0) and 
    (maxI, maxJ)
    
    Args:
        maxI (int): First value limit.
        maxJ (int): Second value limit.
    
    Returns:
        tuple: A random pair of integers between [ (0,0), (maxI, maxJ) ]
    """
    i = randint(0, maxI)
    j = randint(0, maxJ)

    return i, j    