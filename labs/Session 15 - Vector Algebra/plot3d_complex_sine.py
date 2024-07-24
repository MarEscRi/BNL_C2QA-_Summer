#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def f(x: NDArray[np.float_], y: NDArray[np.float_]) -> NDArray[np.float_]:
    """function for |sin z|\n
    input: \n
    x = Re(z) \n
    y = Im(z) \n
    the return value is an expression for the |sin z|, which is provable. 
    """
    return np.array( np.sqrt( np.sin(x) ** 2 + np.sinh(y) ** 2 ) )


def plot(ax: Axes) -> None:
    
    # parameters 
    dp: int  = 100  # number of data points
    R: float = 2.5  # real domain radius
    I: float = 1    # imaginary domain radius

    x: NDArray[np.float_] = np.linspace(-R, R, dp)
    y: NDArray[np.float_] = np.linspace(-I, I, dp)

    ax.set_xlabel("x = Re(z)")
    ax.set_ylabel("y = Im(z)")
    ax.set_zlabel("z")  # type: ignore

    x, y = np.meshgrid(x, y)

    z: NDArray[np.float_] = f(x, y)

    surf: Any = ax.plot_surface(  # type: ignore
        x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False  # type: ignore
    )

    ax.zaxis.set_major_locator(LinearLocator(10))  # type: ignore
    ax.zaxis.set_major_formatter("{x:.02f}")  # type: ignore

    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
