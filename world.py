import cells
import config

def make_world():
    world = []              #Leere Liste für alle Zeilen

    for y in range(config.height):      
        row = []                        
        for x in range(config.width):   
            row.append(cells.make_cell())      

        world.append(row)
    
    return world

def start_new_day(world):       #Resetet jeden Tag, also wenn ein neuer Tag startet sind alle Zellen auf False
    for row in world:
        for cell in row:
            cell["wet"] = False
            cell["sun"] = False
            cell["rain"] = False

def simulate_day(world, random_generator):
    for y, row in enumerate(world):
        for x, cell in enumerate(row):

            if random_generator.random() < config.p_sun:
                cell["sun"] = True
            else:
                cell["sun"] = False 

            effective_rain = config.p_rain
            if cell["sun"]:
                effective_rain = max(0.0, config.p_rain * (1 - config.rain_reduction_when_sun))

            if random_generator.random() < effective_rain:
                cell["rain"] = True
            else:
                cell["rain"] = False
            
            if cell["rain"]:
                cell["wet"] = True


def simulate_night(world):
    pass