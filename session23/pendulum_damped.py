#!/usr/bin/env python3
# pendulum_damped.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator
from scipy.integrate import solve_ivp


def pendulum_model(time, state_vector, phase_constant, damping_constant):
    omega, theta = state_vector  # unpack dependent variables
    d_omega = phase_constant * theta - damping_constant * omega
    d_theta = omega
    return d_omega, d_theta


def plot(ax):
    # Simulation parameters
    time_start = 0  # secs
    time_stop = 10  # secs
    time_step = 0.01  # secs
    time_span = (time_start, time_stop)

    # Initial conditions
    initial_omega = 0  # angular velocity = 0 rad/s (released at rest)
    initial_theta = np.pi / 18  # 10 degrees (small angle)
    initial_conditions = [initial_omega, initial_theta]

    # Constants can be passed to model if they appear in the differential equations
    phase_constant = -9.81 / 1.0  # (m/s^2 = g / pendulum length)

    # Calculate for an underdamped pendulum
    damping_constant = 1.0
    sol = solve_ivp(pendulum_model, time_span, initial_conditions,
                    dense_output=True, max_step=time_step,
                    args=(phase_constant, damping_constant))
    time_array = sol.t
    theta_underdamped_array = sol.y[1]

    # Recalculate using a new constant for an overdamped pendulum
    damping_constant = pow(phase_constant, 2) / 2.0
    sol = solve_ivp(pendulum_model, time_span, initial_conditions,
                    dense_output=True, max_step=time_step,
                    args=(phase_constant, damping_constant))
    theta_overdamped_array = np.copy(sol.y[1])

    # Recalculate using a new constant for a critically damned pendulum
    damping_constant = pow(phase_constant, 2) / 4.0
    sol = solve_ivp(pendulum_model, time_span, initial_conditions,
                    dense_output=True, max_step=time_step,
                    args=(phase_constant, damping_constant))
    theta_criticallydamped_array = np.copy(sol.y[1])

    ax.set_title("Damped Simple Pendulum")
    ax.set_xlabel("time (secs)")
    ax.set_ylabel("theta (radians)")

    ax.axhline(y=0.0, color="lightgray")

    ax.plot(time_array, theta_underdamped_array,
            label='underdamped', color='red', linestyle='solid')
    ax.plot(time_array, theta_overdamped_array,
            label='overdamped', color='blue', linestyle='solid')
    ax.plot(time_array, theta_criticallydamped_array,
            label='critically damped', color='green', linestyle='solid')

    ax.legend(loc="best")

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.figure.savefig("pendulum_damped.png", dpi=600)
    ax.figure.savefig("pendulum_damped.pdf", dpi=600, orientation='landscape')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
