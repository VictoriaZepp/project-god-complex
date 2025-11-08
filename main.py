import config           # lädt die Einstellungen (Größe, Tage, Wahrscheinlichkeiten, Seed)
import cells            # Nachbarn-Funktion
import utils            # Random-Setup + Druckausgabe
import world            # Logik für Tag/Nacht und Welt-Erzeugung


def main():                     #Setup
    rng = utils.random_num()
    grid = world.make_world()
    h, w = len(grid), len(grid[0])


    for day in range(1, config.days +1):
        world.start_new_day(grid)
        world.simulate_day(grid, rng)

        y, x = h // 2, w // 2
        cell = grid[y][x]
        nbrs = cells.get_neighbors(y, x, h, w)
        print(f"Day {day}  cell({y},{x})  sun={cell['sun']} rain={cell['rain']} wet={cell['wet']}")
        print(f"Neighbors: {nbrs}")

        world.simulate_night(grid)



if __name__ == "__main__":
    main()