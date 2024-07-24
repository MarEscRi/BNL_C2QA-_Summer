#!/usr/bin/env python3
"""euler_curve.py"""

from __future__ import annotations

import typing
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import quad # type: ignore

if typing.TYPE_CHECKING: 
    from numpy.typing import NDArray

def cos(u: float) -> float:
    """Integrand associated to x coordinate"""
    r: float = np.cos(u ** 2)
    return r
def sin(u: float) -> float: 
    """Integrand associated to y coordinate."""
    r: float = np.sin(u ** 2)
    return r

def ec(t: float) -> NDArray[np.float_]:
    """
    function that provides eulers curve for a given t
    """

    dp: int = 1000                                  # data points
    u: NDArray[np.float_] = np.linspace(0,t,dp)     # region of integration
    ec: NDArray[np.float_] = np.zeros((2,dp))       # data array containing x(t) and y(t)

    for i in range(dp): 
        # asigning values
        ec[0,i] = quad(cos,0, u[i])[0]
        ec[1,i] = quad(sin,0, u[i])[0]

    return ec

def main() -> None: 

    x: NDArray[np.float_]= ec(12.34)   # data array

    plt.plot(x[0,:],x[1,:],label="Eulers Curve 0 < t < 12.34")
    plt.scatter(.626,.626, color='red', marker='.', label = "Point of convergence (.626,.626)" )

    plt.title("Eulers Curve")
    plt.ylabel(r'$y(t) = \int_0^t \sin(u^2)$d$u$')
    plt.xlabel(r'$x(t) = \int_0^t \cos(u^2)$d$u$')

    plt.grid()
    plt.legend()
    plt.axis('equal')
    plt.show()

if __name__ == "__main__": 
    main()