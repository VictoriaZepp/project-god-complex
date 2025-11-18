class Cell:
    def __init__(self):
        """One place in the grid. It knows its own weather state."""
        self.sun = False
        self.rain = False
        self.wet = False
    
    def reset_new_day(self):
        """Everything starts dry/False again"""
        self.sun = False
        self.rain = False
        self.wet = False
    
    def apply_weather(self, sun: bool, rain: bool):
        """Set weather for today and if it rains wet becomes."""
        self.sun = sun
        self.rain = rain
        if rain:
            self.wet = True
            
    def __repr__(self):
        return f"Cell(sun={self.sun}, rain={self.rain}, wet={self.wet})"