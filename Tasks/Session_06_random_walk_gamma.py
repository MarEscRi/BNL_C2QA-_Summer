#!/usr/bin/env python3
"""random_walk_gamma.py"""

from __future__ import annotations

from math import gamma
import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray

def mean(d: int, N: int) -> NDArray[np.float_]:
    '''
    d = number of dimensions desired \n
    N = number of steps 
    '''

    # The following are the x and y coordinates as arrays encoded in a 2 X n array
    X: NDArray[np.float_] = np.zeros([2, d * 1000 ],float)
    for i in range(d * 1000): 
        X[0,:] = np.linspace(1,d, d * 1000 )
        X[1,i] =  ( (2 * N / X[0,i] ) ** (1 / 2) ) * ( ( gamma(  (X[0,i] + 1) / 2  ) ) / ( gamma( X[0,i]/ 2) ) ) ** 2
    return X


def main() -> None: 
    d: int = 25
    N: int = 20000
    x: NDArray[np.float_] = mean(d,N)
    plt.plot(x[0,:],x[1,:])

    # Format
    plt.title(f"mean value of final distance from the origin")
    plt.xlabel(f"$d$")
    plt.ylabel(f"$E(d)$")
    plt.grid()
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    
    plt.show()

if __name__ == "__main__":
    main()
    