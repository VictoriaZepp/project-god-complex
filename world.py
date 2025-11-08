import cells
import config

def make_world():
    world = []              #Leere Liste für alle Zeilen

    for y in range(config.height):      #jede Zeile
        row = []                        #leere Zeile
        for x in range(config.width):   #Leere Spalte
            row.append(cells.make_cell())      #Füge nun von operations die Zelle zur row hinzu für jede iteration

        world.append(row)
    
    return world

def start_new_day(world):       #Resets everyday to False, frischer start jedes Mal 
    for row in world:
        for cell in row:
            cell["wet"] = False
            cell["sun"] = False
            cell["rain"] = False

def simulate_day(world, random_generator):
    for y,row in enumerate(world):
        for x, cell in enumerate(row):
            cell["sun"] = (random_generator.random() < config.p_sun)
            effective_rain = config.p_rain
            if cell["sun"]:
                effective_rain = max(0.0, config.p_rain * (1 - config.rain_reduction_when_sun)) #Regenwahrscheinlichkeit ggf. reduzieren, wenn Sonne
            cell["rain"] = (random_generator.random() < effective_rain)
            if cell["rain"]:
                cell["wet"] = True


def simulate_night(world):
    pass