import config          
import cells         
import utils            
import world            


def main():                    
    rng = utils.random_num()
    grid = world.make_world()


    for day in range(1, config.days +1):            #Startet hier schon mit 1 und nicht mit 0 
        world.start_new_day(grid)
        world.simulate_day(grid, rng)
        world.simulate_night(grid)



if __name__ == "__main__":
    main()