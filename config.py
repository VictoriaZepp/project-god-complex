#Grid-Größe (2D-Raum)
width = 3       #Anzahl columns (x) → 
height = 3      #Anzahl rows (y) ↓

#Zeit: so viele Tage
days = 3

#Wahrscheinlichkeiten
p_sun = 0.5     #Pro Zelle am Tag
p_rain = 0.4    #Pro Zelle am Tag

# Wenn in der Zelle Sonne scheint, verringert das die Regenchance um diesen Anteil.
# Beispiel: p_rain=0.4 und REDUCTION=0.2 -> effektive Regenchance = 0.4*(1-0.2)=0.32
rain_reduction_when_sun = 0.2

seed = None  # Zufalls-Seed 
