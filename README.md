# Game of Life.
Game of Life if a cellular automaton created by the british mathematician John Conway back in 1970. Although this invention includes the name "Game" this is not a game but a **simulation** of life, based on an initial state of the environment (a grid) and a set of rules. 

These rules are:
1. Any live cell with less than 2 or more than 3 cells around it **dies** because of underpopulation or overpopulation respectively.
2. Any dead cell (empty square in the grid) surrounded by 3 alive cells **lives**.
## Implementation
To improve the performance of the simulations i've done the code for each generation in a very intelligent and efficient way (i think). Instead of checking every cell in the grid to apply the rules of the game I just check the living cells and the cells around those cells. Just with that you can have a fully working implementation of Conway's Game of Life.

Thus, **there's not a matrix** representing the grid **there's just a set of positions where living cells are** in the virtual grid,  which is less memory expensive.
## Getting started.
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites.
To run this project you'll need to install *p5* for Python. Follow this instructions to get it for your machine.
https://p5.readthedocs.io/en/latest/install.html
## Running
Once you have *p5* installed clone the repo and run:
```
python game_of_life -h
```
This will show some help:
* -p [0.0, 1.0]/--population [0.0, 1.0]: Percentage of the cells of the grid that are alive (0.2 by default).
* -s [SIZE]/--size [SIZE]: Size of the squared grid (30 by default).

Once you run the program a window will open showing the environment. **You can start the simulation** by pressing the *spacebar*. You can also stop it doing so. Additionaly you can **add a living cell by clicking** at any position of the grid.
### Examples
The example below will start an instance of game of life with a grid of 50x50 and a 40% of the cells alive.
```
python game_of_life -p 0.4 -s 50
```

## Contribute
Feel free to contribute and suggest new ideas for the project.
