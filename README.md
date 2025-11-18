# project-god-complex
config.py: 
I first thought about how to create the size of the world. I imagined a 2D world (matrix) where x are cloumns (width) and y are rows(height). I added how many days I want to run my file. Also the probabilities of rain und sun and the condition when the sun is shining its x percent less likely that it rains. I set the seed as None so that the weather changes for every run. 

cells.py:
The function make_cell() describes how one cell looks. Before the first day starts everything is set to False because there is no sun or rain yet and the cell is still dry.
The function get_neighbors checks which cells are next to a cell. 
I used a print statement to check if the function get_neighbors() really finds the correct neighboring cells.

world.py:
I create the 2D world. It is a grid made of rows (y) and columns (x) -> For loop
Each place in the grid is one cell that comes from cells.make_cell() For every row and column it adds one new cell.
Tested it with a print statement again. 
start_new_day(): Resets cells at the beginning of each day 
def simulate_day: Basically I go through my matrix and look at the random number it generated (between 0 and 1) if it is smaller than my probabilities I set in my utils.py file. If that is the case the cell now has the boolean True. 

utils.py:
def random_num(): creates my random number generator for seeds. If I set seed to a number it will always give me back the same random numbers. If I set it to None it will give me back new random numbers for every day. 
I tested this by printing random numbers and seeing that they change when I run the program again.




