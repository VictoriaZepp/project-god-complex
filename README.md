# project-god-complex
config.py: 
Defines the Config class, which stores all parameters of the simulation (grid size, number of days, probabilities, seed).
I set seed=None so the weather results change every time I run the program. If I assign a fixed seed, the simulation becomes repeatable.

cells.py:
Contains the class Cell. 
Every cell has its own state (if it had sun or rain today).
Method apply_weather() updates the cell based on the weather it receives.

world.py:
World Class creates a 2D grid made of Cell objects.
simulate_day() loops over all cells and randomly decides if they get sun or rain.
neighbors() returns the neighboring cells of a given position inside the grid.

main.py:
I create a Config object and a World object and then I run the simulation.
At the end I print out some example values (like the center cell and its neighbors).



