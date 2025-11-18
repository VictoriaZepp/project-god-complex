class Config:
    """Speichert Einstellungen: Breite, Höhe, Tage, Wahrscheinlichkeiten."""
    def __init__(self,
                  width=3,
                  height=3,
                  days=3,
                  p_sun=0.5,
                  p_rain=0.4,
                  rain_reduction_when_sun=0.2,
                  seed=None):
        self.width = width
        self.height = height
        self.days = days
        self.p_sun = p_sun
        self.p_rain = p_rain
        self.rain_reduction_when_sun = rain_reduction_when_sun 
        self.seed = seed
    
    def __repr__(self):
        return (f"Config(width={self.width}, height={self.height}, "
                f"days={self.days}, p_sun={self.p_sun}, "
                f"p_rain={self.p_rain}, rain_reduction_when_sun={self.rain_reduction_when_sun}, "
                f"seed={self.seed})")


