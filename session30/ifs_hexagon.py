#!/usr/bin/env python3
# ifs_hexagon.py

import numpy as np
from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem

ifs = IteratedFunctionSystem()


def plot_triangle_ifs(ss):
    iterations = 200_000
    x, y = 0, 0

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, color = ifs.transform_point(x, y)

    for _ in range(iterations):
        x, y, color = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, color)


def main():
    ifs.set_base_frame(0, 0, 30, 30)

    p = 1 / 6

    # TODO: Edit this mappings according to the Cartesian coordinates
    ifs.add_mapping(0, 0, 0, 0, 0, 0, "blue", p)		# COD
    ifs.add_mapping(0, 0, 0, 0, 0, 0, "blue", p)        # DOE
    ifs.add_mapping(0, 0, 0, 0, 0, 0, "blue", p)		# EOF
    ifs.add_mapping(0, 0, 0, 0, 0, 0, "blue", p)		# FOA
    ifs.add_mapping(0, 0, 0, 0, 0, 0, "blue", p)        # AOB
    ifs.add_mapping(0, 0, 0, 0, 0, 0, "blue", p)		# BOC

    ifs.generate_transforms()

    ss = SimpleScreen(world_rect=((0, 0), (30, 30)),
                      screen_size=(1000, 1000),
                      draw_function=plot_triangle_ifs,
                      title='Hexagon Shape')
    ss.show()


if __name__ == "__main__":
    main()
