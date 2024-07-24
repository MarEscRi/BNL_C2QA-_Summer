#!/usr/bin/env python3
"""eulers_constant.py"""

from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad  # type: ignore

import typing

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray

def f(x: float) -> float:
    """
    function used to calculate Eulers constant
    """
    r: float = -np.log(np.log(1 / x))
    return r


def ps(n: int) -> list[float]:
    r: list[float] = []
    s: float = 0
    for i in range(1, n + 1):
        s += 1 / i
        r.append(s)
    return r


def main() -> None:
    # Eulers constant
    gamma: float = quad(f, 0, 1)[0]

    # data points
    d: int = 1_000

    # Generating data array
    x: NDArray[np.float_] = np.zeros((2, d))

    # Assigning values to x[0,:]
    x[0, :] = np.linspace(1, 50, d)

    # Assigning values to x[1,:]
    x[1, :] = gamma + np.log(x[0, :])

    # Ploting for partial sums of harmonic
    a: NDArray[np.int_] = np.arange(1, 51)
    t: list[float] = ps(50)

    plt.plot(x[0, :], x[1, :], label="Harmonic Numbers")
    plt.step(a, t, label="Natural Logarithm")
    plt.title("Harmonic Numbers")
    plt.xlabel("n")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()