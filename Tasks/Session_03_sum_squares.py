#!/usr/bin/env python3
"""sum_squares.py"""

# function for calculating partial sum of natural numbers squared (will be called sum)
def sum(n:int) -> float: 
    """
    n = the number you wish to sum to \n
    s = the value of the sum 
    """ 

    s:float = 0.0
    for i in range(1,n + 1):
        s += i ** 2

    return s

def main() -> None: 

    n: int = 1_000
    
    # P = Gauss formula for the sum of the sum of natural number squared 
    P:float = ( 2 * n ** 3 + 3 * n ** 2 + n ) / 6

    print(f"The value of the partial sum for the first", f"{n:,.0f}", f"natural numbers is", f"{sum(n):,.0f}." )
    print(f"We know double check using Gauss' formula for the sum of natural numbers squared. Obtaining ", f"{P:,.0f}")

if __name__ == "__main__":
    main()
