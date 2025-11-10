def make_cell():                                        
    return{"sun": False, "rain": False, "wet": False}   #Vor dem ersten Tag (begin) ist noch nichts deshlab False 

def get_neighbors(y, x, height, width):     #schaut ob es links, rechts, oben oder unten eine Nachbarzelle gibt
    nbrs = []                           
    if x - 1 >= 0:
        nbrs.append((y, x-1))           #links
    if x + 1 < width:
        nbrs.append((y, x+1))           #rechts
    if y - 1 >= 0:
        nbrs.append((y-1, x))           #oben
    if y + 1 < height:
        nbrs.append((y+1, x))           #unten
    return nbrs

