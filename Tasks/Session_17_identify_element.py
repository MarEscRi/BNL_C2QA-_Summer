#!/usr/bin/env python3
"""identify_element.py"""

# This program was authored by Dr. David Biersach

from __future__ import annotations
import typing
import matplotlib.pyplot as plt 
import numpy as np 
from pathlib import Path
if typing. TYPE_CHECKING:
    from matplotlib.axes import Axes 
    from numpy. typing import NDArray

def fit_linear(x: NDArray[np.float_], y: NDArray[np.float_]) -> tuple[float, float]:
    n: int = len(x)
    m: float = float (n * np.sum(x * y) - np.sum(x) * np.sum(y))
    m /= float(n * np.sum(x ** 2) - np.sum(x) ** 2)
    b: float = float (np.sum(y) - m * np. sum(x))
    b /= n
    return m, b

def plot (ax: Axes) -> None:
    # Parse the data file
    data_file: Path = Path(__file__).parent.joinpath("gas.csv") 
    data: NDArray[np.float_] = np.genfromtxt (
        data_file, delimiter= ",",skip_header=1, dtype=np.float_    
    )

    # Convert experimental data to SI units
    temperature: NDArray [np. float_] = data[:, 0] + 273.15 # 1st column to kelvin
    volume: NDArray [np.float_] = data[:, 1] / 1000 # 2nd column to meters cubed
    # Calculate slope of best-fit line

    m: float
    b: float
    m, b = fit_linear (temperature, volume)

    # Apply Ideal gas law
    p: float = 2.0 * 101_325 # Convert 2.0 atm (given) to pascals
    r = 8.31446261815324  # Gas constant (SI units)
    n: float = p / r * m # Moles of gas (rearrange ideal gas law equation)

    # Calculate atomic mass of sample using number of moles
    m_sample = 50 # (given) grams
    molar_mass: float = m_sample / n # sample mass divided by number of moles

    # Plot experimental data
    ax.scatter (temperature, volume, color="red")

    # Draw line of best fit
    x: NDArray [np. float_] = np. linspace(0, 500, 1000)
    ax.plot(x, m * x + b)

    ax.set_title(f"Unknown Gas ({molar_mass: .3f}u)")
    ax.set_xlabel(r"$Temperature\; (\degree K)$") 
    ax.set_ylabel(r"$volumel; (m^3)$")

def main() -> None:
    plt.figure(__file__)
    plot (plt.axes ())
    plt.show()

if __name__ == "main":
    main()