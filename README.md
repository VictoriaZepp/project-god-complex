# project-god-complex
config.py: 
I first thought about how to create the size of the world. I imagined a 2D world where x are cloumns (width) and y are rows(height). I added how many days I want to run my file. Also the probabilities of rain und sun and the condition when the sun is shining its x percent less likely that it rains. I set the seed as None so that the weather changes for every run. 


cells.py:
The function make_cell() describes how one cell looks.
At the beginning, before the first day starts, everything is set to False
because there is no sun or rain yet and the cell is still dry.

The function get_neighbors(y, x, height, width) checks which cells are next to a given cell —
left, right, top, or bottom.
It returns only the valid neighboring cells inside the grid.
I tested the function get_neighbors() with different coordinates to see if it really finds the correct neighboring cells.
I used simple print() statements to check the output in the terminal.
print(get_neighbors(1, 1, 3, 3))

world.py


