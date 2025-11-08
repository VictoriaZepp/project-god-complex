# project-god-complex
config.py: 
I first thought about how to create the size of the world. I imagined a 2D world where x are cloumns (width) and y are rows(height). I added how many days I want to run my file. Also the probabilities of rain und sun and the condition when the sun is shining its x percent less likely that it rains. I set the seed as None so that the weather changes for every run. 

cells.py:
The function make_cell() describes how one cell looks. Before the first day starts everything is set to False because there is no sun or rain yet and the cell is still dry.
The function get_neighbors(y, x, height, width) checks which cells are next to a cell. 
I tested the function get_neighbors() with different coordinates to see if it really finds the correct neighboring cells.
For that I used a print statement 
print(get_neighbors(1, 1, 3, 3))

world.py:
Now I create the 2D world. It is a grid made of rows (y) and columns (x) -> For loop
Each place in the grid is one cell that comes from cells.make_cell() For every row and column, it adds one new cell.
To test if the world works I used the print statement. 
start_new_day(): Resets cells at the beginning of each day 
def simulate_day(world, random_generator):  Basically I go through my matrix and look at the random number it generated (between 0 and 1) if it is smaller than my probabilities I set in my utils.py file. If that is the case the cell now has the boolean True. 

utils.py:
def random_num(): creates my random number generator for seeds. If I set seed to a number it will always give me back the same random numbers. If I set it to None it will give me back new random numbers for every day. 
I tested this by printing random numbers and seeing that they change when I run the program again.
print_world(): prints my 2D world as symbols in the terminal.
. means nothing happens 




