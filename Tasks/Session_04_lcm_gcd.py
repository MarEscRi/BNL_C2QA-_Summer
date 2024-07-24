#!/usr/bin/env python3
"""lcm_gcd.py"""

from math import gcd


def lcm(a:int, b:int) -> float: 
    '''
    This function provides the least common multiple of a and b 
    '''

    # g is the greatest common divisor of a and b
    g: int = gcd(a,b)

    # the following formula is a provable statement
    # and can by found in page 13, problem 31.b
    # of "Abstract Algebra: An Introduction" by Hungerford
    l: float = ( a * b ) / g  

    return l

def main() -> None:

    # The numbers you want to the lcm of
    a: int = 447618
    b: int = 2011835

    print(f"lcm( {a:,} ; {b:,} ) = {lcm(a,b):,}")

if __name__ == "__main__":
    main()

