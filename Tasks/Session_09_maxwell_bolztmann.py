#!/usr/bin/env python3
"""maxwell_bolztmann.py"""
from __future__ import annotations
import numpy as np 
import typing 
import matplotlib.pyplot as plt

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray

def MB(a: float) -> NDArray[np.float_]: 
    """
    Maxwell-Bolztmann Probability Density \n
    Provides MB PDF in a domain of [0,20] for a given a
    """

    # Number of data points 
    n: int = 1000 

    # Constructing input and output array
    x: NDArray[np.float_] = np.zeros((2,n),float) 

    # assigning input output values
    x[0,:]= np.linspace(0,20,n)
    x[1,:] = np.sqrt( 2 / np.pi ) * ( np.power(x[0,:],2) / np.power(a,3) ) * np.exp( - np.power((x[0,:]/a),2) * .5 )

    return x 

def main() -> None: 

    # MB PDF for a = 1, a = 2 and a = 3
    a1: NDArray[np.float_] = MB(1)
    a2: NDArray[np.float_] = MB(2)
    a5: NDArray[np.float_] = MB(5)

    # Ploting all three PDFs
    plt.plot( a1[0,:] , a1[1,:] , label = rf"$a = 1$")
    plt.plot( a1[0,:] , a2[1,:] , label = rf"$a = 2$")
    plt.plot( a1[0,:] , a5[1,:] , label = rf"$a = 5$")
    
    plt.title("Maxwel-Bolztmann Probability Density")
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()