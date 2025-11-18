import random
from cell import Cell

class World:
    """2D grid of cells + day/night cycle"""
    def __init__(self, config):
        self.cfg = config
        if self.cfg is not None:
            random.seed(self.cfg.seed)
        self.grid = [[Cell() for _ in range(self.cfg.width)]            #erstellt das Gitter. Die äußere Schleife macht Zeilen (height), die innere Schleife macht Spalten (width).
                     for _ in range(self.cfg.height)]
        self.is_day = True                                              #Welt beginnt am Tag, True bedeutet Tag

#---------Raum/Position-------------------
    def in_bounds(self, y, x) -> bool:
        return 0 <= y < self.cfg.height and 0 <= x < self.cfg.width
    def neighbors(self, x, y):
        nbrs = []
        for ny, nx in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
            if self.in_bounds(ny, nx):
                nbrs.append((ny,nx))
            return nbrs
        
#-----------Zeit/Wetter------------------
    def start_new_day(self):
        for row in self.grid:
            for cell in row:
                cell.reset_new_day()                        #Das setzt die Zelle wieder auf den Anfangszustand
        self.is_day = True                                  #nach dem Reset ist es jetzt wieder Tag
    
    def simulate_day(self):
        for row in self.grid:
            for cell in row:
                sun_today = (random.random() < self.cfg.p_sun)
                effective_rain = self.cfg.p_rain            #Regenchance reduziert wenn es sonnig ist.
                if sun_today:
                    effective_rain = self.cfg.p_rain * (1 - self.cfg.rain_reduction_when_sun)
                rain_today = (random.random() < effective_rain)
                cell.apply_weather(sun_today, rain_today)           #übergibt das Ergebnis an die Zelle
                
    def simulate_night(self):
        self.is_day = False
    
    def simulate(self, days: int):
        for _ in range(days):
            self.start_new_day()
            self.simulate_day()
            self.simulate_night()
