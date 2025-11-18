class Cell:
    """stellt eine Position im Raster dar"""
    def __init__(self):
        """Zelle kennt seinen eigenen Wetterzustand."""
        self.sun = False
        self.rain = False
        self.wet = False
    
    def reset_new_day(self):
        """Alles startet trocken/falsch wieder."""
        self.sun = False
        self.rain = False
        self.wet = False
    
    def apply_weather(self, sun: bool, rain: bool):
        """Setzt Wetter für heute und falls es regnet ist es nass."""
        self.sun = sun
        self.rain = rain
        if rain:
            self.wet = True
            
    def __repr__(self):
        return f"Cell(sun={self.sun}, rain={self.rain}, wet={self.wet})"