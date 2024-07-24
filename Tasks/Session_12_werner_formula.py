#!/usr/bin/env python3
"""werner_formula.py"""

from __future__ import annotations
import numpy as np 
import matplotlib.pyplot as plt
import typing 
if typing.TYPE_CHECKING: 
    from numpy.typing import NDArray

def F(dp: int) -> NDArray[np.float_]:
    """
    Function that generates an array containing the outputs of four specified functions \n
    dp = the amount of desired points
    """

    # Generation of Data Array
    x: NDArray[np.float_] = np.zeros((5,dp))

    # Defining rows of data array  
    x[0,:] = np.linspace(-3 * np.pi , 3 * np.pi, dp) # input 
    x[1,:] = np.sin( 0.8 * x[0,:] ) # f1
    x[2,:] = np.sin( 0.5 * x[0,:] ) # f2
    x[3,:] = np.sin( 0.8 * x[0,:] ) * np.sin( 0.5 * x[0,:] ) # f3
    x[4,:] = 0.5 * ( np.cos( 0.3 * x[0,:] ) - np.cos( 1.3 * x[0,:] ) ) # f4

    return x

def main() -> None: 

    # Data points
    dp: int = 10_000

    # Defining information array 
    x: NDArray[np.float_] = F(dp)[0,:]
    f1: NDArray[np.float_] = F(dp)[1,:]
    f2: NDArray[np.float_] = F(dp)[2,:]
    f3: NDArray[np.float_] = F(dp)[3,:]
    f4: NDArray[np.float_] = F(dp)[4,:]

    plt.plot(x,f1, label = r'$\sin{0.8 x}$')
    plt.plot(x,f2, label = r'$\sin{0.5 x}$')
    plt.plot(x,f3, label = r'$\sin( 0.8  x) \sin( 0.5  x)$', linewidth = 2.5)
    plt.scatter(x,f4, label = r'$0.5 (\cos{ 0.3  x} - \cos{ 1.3  x})$' , marker='o', edgecolors='black', facecolors='none')

    plt.title("Graphs of Sinusoidal functions")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()