from config import Config
from world import World

def main():
    cfg = Config(
        width=3,
        height=3,
        days=3,
        p_sun=0.5,
        p_rain=0.4,
        rain_reduction_when_sun=0.2,
        seed=None
    )

    w = World(cfg)

    w.simulate(cfg.days)

    y = cfg.height // 2                 #gibt mittlere Position des Grid an ohne Kommazahlen, Hardcoded 1 würde nur bei einem 3x3 Grid funktionieren.
    x = cfg.width // 2

    print("Center:", w.grid[y][x])
    print("Neighbors:", w.neighbors(y, x))

if __name__ == "__main__":
    main()