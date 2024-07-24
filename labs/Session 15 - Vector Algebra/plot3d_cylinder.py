#!/usr/bin/env python3
"""plot3d_cylinder.py"""

# "plot3d_sphere.py" was used as a starting point for this program

from __future__ import annotations
import typing
import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:

    # important parameters
    dp: int  = 30    # data points in graph
    h: float = 2     # height of cylinder
    s: float = 1.0   # cylindrical radius

    # azimuthal angle
    phi: NDArray[np.float_] = np.linspace(0, 2 * np.pi, dp)

    # height array
    Z: NDArray[np.float_] = np.linspace(-h / 2, h / 2, dp)

    # Creation of coordinates for the cylinder surface
    x: NDArray[np.float_] = np.outer(np.cos(phi), s)
    y: NDArray[np.float_] = np.outer(np.sin(phi), s)
    z: NDArray[np.float_] = np.outer(np.ones_like(phi), Z)

    # Ploting
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    # TODO: Uncomment the following lines one-by-one
    # ax.scatter(x, y, z)
    ax.plot_wireframe(x, y, z)  # type: ignore
    # ax.plot_surface(x, y, z)  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
