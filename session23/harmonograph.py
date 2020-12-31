#!/usr/bin/env python3
# harmonograph.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator
from numpy.core.numeric import NaN

phase_constant = NaN


def d_omega(omega, theta, time):
    return phase_constant * theta


def d_theta(omega, theta, time):
    return omega


def rk4(v1, v2, u, h, f1, f2):
    # Implements 4th order Runge-Kutta method
    # for two linked ODEs (f1 and f2), sharing
    # the dependent variables (v1, v2) and the
    # independent variable (u) having step size (h)
    k1_v1 = f1(v1, v2, u)
    k1_v2 = f2(v1, v2, u)

    k2_v1 = f1(v1 + (h / 2.0) * k1_v1, v2 + (h / 2.0) * k1_v2, u)
    k2_v2 = f2(v1 + (h / 2.0) * k1_v1, v2 + (h / 2.0) * k1_v2, u)

    k3_v1 = f1(v1 + (h / 2.0) * k2_v1, v2 + (h / 2.0) * k2_v2, u)
    k3_v2 = f2(v1 + (h / 2.0) * k2_v1, v2 + (h / 2.0) * k2_v2, u)

    k4_v1 = f1(v1 + h * k3_v1, v2 + h * k3_v2, u)
    k4_v2 = f2(v1 + h * k3_v1, v2 + h * k3_v2, u)

    next_v1 = v1 + h * (k1_v1 + 2.0 * k2_v1 + 2.0 * k3_v1 + k4_v1) / 6.0
    next_v2 = v2 + h * (k1_v2 + 2.0 * k2_v2 + 2.0 * k3_v2 + k4_v2) / 6.0
    next_u = u + h

    return next_v1, next_v2, next_u


def plot(ax):
    global phase_constant

    time_stop = 10  # seconds
    time_steps = 250
    delta_time = time_stop / time_steps

    omega_array = np.zeros(time_steps)
    theta_array = np.zeros(time_steps)
    time_array = np.zeros(time_steps)

    phase_constant = -9.81 / 1.0  # (m/s^2 = g / pendulum length)

    omega_array[0] = 0                # angular velocity = 0 (released at rest)
    theta_array[0] = np.pi / 18     # 10 degrees (small angle)
    time_array[0] = 0                 # set initial time value

    omega = omega_array[0]
    theta = theta_array[0]
    time = time_array[0]

    for step in range(1, time_steps):
        omega, theta, time = rk4(
            omega, theta, time, delta_time, d_omega, d_theta)
        omega_array[step] = omega
        theta_array[step] = theta
        time_array[step] = time

    # Setup the 2nd pendulum
    omega2_array = np.zeros(time_steps)
    theta2_array = np.zeros(time_steps)

    phase_constant = -9.81 / 1.5  # (m/s^2 = g / pendulum length)

    omega2_array[0] = 0             # angular velocity = 0 (released at rest)
    theta2_array[0] = np.pi / 18    # 10 degrees (small angle)

    omega = omega2_array[0]
    theta = theta2_array[0]
    time = time_array[0]

    for step in range(1, time_steps):
        omega, theta, time = rk4(
            omega, theta, time, delta_time, d_omega, d_theta)
        omega2_array[step] = omega
        theta2_array[step] = theta

    ax.set_title("Two Pendulum Harmonograph (RK4 Method)")
    ax.set_xlabel("theta (radians)")
    ax.set_ylabel("theta2 (radians)")

    ax.plot(theta_array, theta2_array, color='blue', linestyle='solid')

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.figure.savefig("harmonograph.png", dpi=600)


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
