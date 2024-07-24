#!/usr/bin/env python3
"""ifs_hexagonal.py"""

# this code borrows from other code "ifs_triangle.py" and Dr. Davis Biersach
import numpy as np 
from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()

def plot_ifs(ss: SimpleScreen) -> None:
    iterations = 200_000
    x: float = 0.0
    y: float = 0.0
    clr: Color

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)

def main() -> None:
    ifs.set_base_frame(0, 0, 30, 30)

    h: float = 5 * np.sqrt(3)
    p: float = 1 / 6

    # mappings 
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + h, Color("blue"), p)        # COD
    ifs.add_mapping(20, 15 + h, 15, 15, 10, 15 + h, Color("blue"), p)    # DOE
    ifs.add_mapping(10, 15 + h, 15, 15, 5, 15, Color("blue"), p)         # EOF
    ifs.add_mapping(5, 15, 15, 15, 10, 15 - h, Color("blue"), p)         # FOA
    ifs.add_mapping(10, 15 - h, 15, 15, 20, 15 - h, Color("blue"), p)    # AOB
    ifs.add_mapping(20, 15 - h, 15, 15, 25, 15, Color ("blue"), p)       # BOC

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Square",
    )
    ss.show()


if __name__ == "__main__":
    main()
