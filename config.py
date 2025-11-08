width = 3       #Anzahl columns (x) → 
height = 3      #Anzahl rows (y) ↓

#so viele Tage
days = 3

#Wahrscheinlichkeiten
p_sun = 0.5     
p_rain = 0.4    

#Wenn sun = True reduziert es die Wahrscheinlichkeit, dass es regnet
#Beispiel: p_rain=0.4 und rain_reduction_when_sun=0.2 -> Regenchance = 0.4*(1-0.2)=0.32
rain_reduction_when_sun = 0.2

seed = None  # Zufalls-Seed, bei None ist es immer verschieden
