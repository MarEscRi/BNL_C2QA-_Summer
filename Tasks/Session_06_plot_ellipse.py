#!/usr/bin/env python3 
"""plot_ellipse.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray

def ellipse(a: float, b: float) -> NDArray[np.float_]:
    '''
    a = major axis \n
    b = minor axis
    '''
    # n = the amount of points used
    n = 1000

    # Theta = parameter of the functios 
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi , n)

    # The following are the x and y coordinates as arrays encoded in a 2 X n array
    x: NDArray[np.float_] = np.zeros([2,n],float)
    x[0,:] = a * np.cos(theta) 
    x[1,:]= b * np.sin(theta) 

    return x 

# python started complaining when I tried returning multiple values 

def main() -> None: 
    a: float = 100 
    b: float = 50
    x: NDArray[np.float_] = ellipse(a,b)
    plt.plot(x[0,:],x[1,:])

    # Format
    plt.title(rf'$\frac{{x^2}}{{{a}^2}} + \frac{{x^2}}{{{b}^2}} = 1$')
    plt.xlabel(f"$x$")
    plt.ylabel(f"$y$")
    plt.grid()
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    
    plt.axis("equal")
    plt.show()

if __name__ == "__main__":
    main()