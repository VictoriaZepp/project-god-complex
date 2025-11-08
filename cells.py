#operations.py ist wie eine Werkzeugkiste für die kleinsten Bauteile der Welt:

def make_cell():                                        #Beschreibt wie eine Zelle aussieht und startet
    return{"sun": False, "rain": False, "wet": False}   #Vor dem ersten Tag (begin) ist noch nichts deshlab False 

def get_neighbors(y, x, height, width):     #schaut, ob links, rechts, oben oder unten eine gültige Nachbarzelle existiert.
    nbrs = []                           #starten mit leerer Nachbarzelle
    if x - 1 >= 0:
        nbrs.append((y, x-1))           #links
    if x + 1 < width:
        nbrs.append((y, x+1))           #rechts
    if y - 1 >= 0:
        nbrs.append((y-1, x))           #oben
    if y + 1 < height:
        nbrs.append((y+1, x))           #unten
    return nbrs

