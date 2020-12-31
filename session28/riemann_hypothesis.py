#!/usr/bin/env python3
# riemann_hypothesis.py

import numpy as np
import matplotlib.pyplot as plt


def eta_term(s: complex, n: np.int) -> np.complex:
    return np.complex(1 / np.power(n, s))


vec_eta_term = np.vectorize(eta_term)


def fn_eta(s: np.complex) -> np.complex:
    terms = int(1e5)
    eta = (np.complex(1)
           - np.sum(vec_eta_term(s, np.arange(2, terms, 2, dtype=np.int)))
           + np.sum(vec_eta_term(s, np.arange(3, terms, 2, dtype=np.int))))
    return eta


def fn_zeta_from_eta(s: np.complex) -> np.complex:
    return s / (1.0 - np.power(2, 1.0 - s))


def plot(ax):
    xa = np.linspace(-1, 27, 800)
    xz = [np.complex(0.5, i) for i in xa]

    eta = [fn_eta(s) for s in xz]
    zeta = [fn_zeta_from_eta(s) for s in eta]

    ax.plot(xa, np.absolute(eta),
            label=r'$\zeta \left( s \right)$')
    ax.plot(xa, np.absolute(zeta),
            label=r'$\eta \left( s \right)$', color='red')

    zeta_zeros_im = [14.134725141, 21.022039638, 25.010857580, 30.424876125]
    ax.scatter(zeta_zeros_im, [0]*len(zeta_zeros_im),
               marker='o', color='green', label=r"$\zeta\ root$")

    ax.set_title(r"$Riemann\ Zeta\ vs.\ Dedekind\ Eta$")
    ax.set_xlabel(r'$\mathrm{Im}\{s\}$')  # (r'$\Im{s}$') for {physics}
    ax.set_ylabel(r'$\left|s\right\|$')
    ax.legend(loc='best')
    ax.set_axisbelow(True)
    ax.grid(color='gray', linestyle='dashed')

    ax.figure.set_size_inches(11, 8.5)
    ax.figure.savefig(f"riemann_hypothesis.png", dpi=600)
    ax.figure.savefig(f"riemann_hypothesis.pdf", dpi=600,
                      orientation='landscape')


def main():
    # To switch from matplotlib's built-in "mathtext" to a
    # true LaTex package, uncomment these next three lines:
    # import matplotlib
    # matplotlib.rcParams['text.usetex'] = True
    # matplotlib.rcParams['text.latex.preamble'] = r"\usepackage{physics}"

    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
