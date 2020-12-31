#!/usr/bin/env python3
# projectile_motion.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation


def plot(ax):
    global xa, ya, line

    range = 400             # m
    theta = np.radians(45)  # 45 degree launch angle
    g = 9.81                # m/s^2

    # Initial velocity (m/s)
    # TODO: Edit the next line of code
    v0 = 45

    xa = np.linspace(0, 600, 200)
    ya = np.tan(theta) * xa - (g / (2 * v0**2 * np.cos(theta)**2)) * xa**2

    line, = ax.plot(xa, ya)

    ax.set_title("Ideal Projectile Motion")
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel("Height (m)")
    ax.set_ylim(bottom=0)
    ax.set_xlim(left=0)

    ax.add_patch(Rectangle((395, 0), 10, 2, color='red'))


def anim_frame_counter():
    global anim_continue
    anim_continue = True
    n = 0
    while anim_continue and n < len(xa):
        n += 1
        yield n


def anim_draw_frame(n):
    global anim_continue
    line.set_data(xa[:n], ya[:n])
    if n > 0:
        if ya[n-1] < 0:
            anim_continue = False
            if xa[n-1] < 398 or xa[n-1] > 408:
                print("Splat!")
            else:
                print("Safe landing!")
    return line,


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])

    plot(ax)

    anim = FuncAnimation(ax.figure, anim_draw_frame, anim_frame_counter,
                         interval=25, blit=True, repeat=False)

    plt.show()


if __name__ == "__main__":
    main()
