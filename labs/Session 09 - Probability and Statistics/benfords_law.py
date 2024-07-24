#!/usr/bin/env python3
"""benfords_law.py"""

from __future__ import annotations
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
import typing

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def dp(nd: int) -> NDArray[np.float_]:
    """
    digit probability \n
    Input: \n
    nd = number of randomly generated numbers \n
    Output: \n
    x = 3 x 9 array \n
    x[0,:] = digits from 1 to 9 \n
    x[1,:] = number of times said digit appeared as significant digit \n
    x[2,:] = associated probability
    """

    # Constructing data array
    x: NDArray[np.float_] = np.zeros((3, 9))

    # assigning x[0,:]
    x[0, :] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Defining a kronecker delta
    kd: NDArray[np.float_] = np.identity(9)

    # Array that generates random integers
    s: NDArray[np.int_] = randint(1, 1_000_000, nd)
    s[:] = s[:] ** 2

    # obtaining value of x[1,:]
    for i in range(0, nd):
        # Significant digit associates to integer s[i]
        t: int = int(str(s[i])[0])

        # Using Kronecker delta to count (as to avoid if statements)
        x[1, 0] += kd[0, t - 1]
        x[1, 1] += kd[1, t - 1]
        x[1, 2] += kd[2, t - 1]
        x[1, 3] += kd[3, t - 1]
        x[1, 4] += kd[4, t - 1]
        x[1, 5] += kd[5, t - 1]
        x[1, 6] += kd[6, t - 1]
        x[1, 7] += kd[7, t - 1]
        x[1, 8] += kd[8, t - 1]

    # Calculating x[2,:]
    x[2, 0] = x[1, 0] / nd
    x[2, 1] = x[1, 1] / nd
    x[2, 2] = x[1, 2] / nd
    x[2, 3] = x[1, 3] / nd
    x[2, 4] = x[1, 4] / nd
    x[2, 5] = x[1, 5] / nd
    x[2, 6] = x[1, 6] / nd
    x[2, 7] = x[1, 7] / nd
    x[2, 8] = x[1, 8] / nd

    return x


def main() -> None:
    x: NDArray[np.float_] = dp(100_000)

    plt.bar(x[0, :], x[2, :], width=0.5)

    plt.title("Significant Digit Probability")
    plt.ylabel("probability")
    plt.xlabel("digits")

    plt.xticks(x[0, :])
    plt.yticks([0.01, 0.03, 0.05, 0.07, 0.09, 0.11])
    plt.grid(axis="y")

    plt.show()


if __name__ == "__main__":
    main()
