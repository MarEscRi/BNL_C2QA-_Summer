#!/usr/bin/env python3
"""plot_trajectory.py"""

# Dr. David Biersach is the source of this code
from __future__ import annotations

import typing
import numpy as np 
import matplotlib.pyplot as plt 

from pathlib import Path

if typing. TYPE_CHECKING:
    from matplotlib.axes import Axes 
    from numpy.typing import NDArray


def fit_linear (x: NDArray [np.float_], y: NDArray [np.float_]) -> tuple[float, float]:
    n: int = len (x)
    m: float = float(n * np. sum(x * y) - np.sum(x) * np. sum(y))
    m /= float( n * np.sum( x ** 2 ) - np.sum(x) ** 2 )
    b: float = float (np.sum(y) - m * np. sum(x))
    b /= n
    return m,b

def plot(ax: Axes) -> None:

    data_file: Path = Path(__file__).parent.joinpath("ray.csv")
    data = np.genfromtxt (data_file, delimiter=",") # type: Ignore

    X = data[:, 0] # type: Ignore # time in nanoseconds 
    y = data[:, 1] # type: Ignore # height in centimeters

    m: float
    b: float
    m, b = fit_linear(X, y)
    h = (np.abs (m) * 1e9 / 100) * (0.1743 / 1e3) / 1000
    c = 29.98 # speed of light in cm/ns

    print (f"Slope = {abs(m):.4f} cm/ns")
    print (f"Velocity = {np.abs(m)/c:,.2f} c")
    print (f"Origination Height = {h:,.2f} km")

    ax.scatter(X, y)
    ax.plot(X, m * X + b, color="red", linewidth=2) 

    ax. set_title("Secondary Cosmic Ray Trajectory") 
    ax.set_xlabel("time (ns)") 
    ax.set_ylabel("height (cm)") 
    ax.grid()

def main() -> None: 
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()