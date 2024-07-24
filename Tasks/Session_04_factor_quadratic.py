#!/usr/bin/env python3
"""factor_quadratic.py"""

from math import gcd, floor

def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""

    print(f"Given the quadratic: {h:,}x^2 + {i:,}x + {j:,}")

    print(f"The shared gcd of {h:,}; {i:,} and {j:,} is { gcd( gcd( h , i ) , j ) :,}")

    # the following is the discriminant, from the quadratic ecuation 
    dis: float = i ** 2 - 4 * h * j

    # How to identify complex solutions
    if dis < 0: 
        print(f"Your quadratic has no factorization over the real number")

    # How to identify irrational solutions
    if dis ** (1/2) - floor(dis ** (1/2)) != 0:
        print(f"Your quadratic has no factorization over the integers")

    for a in range(1, h + 1):
        if h % a == 0:
            c: int = h // a
            for b in range(1, j + 1):
                if j % b == 0:
                    d: int = j // b
                    if a * d + b * c == i:
                        print(f"The factors are: ({a:,}x + {b:,})({c:,}x + {d:,})")
                        return
                    

def main() -> None:
    h: int = 115425
    i: int = 3254121
    j: int = 379021
    factor_quadratic(h,i,j)
    

if __name__ == "__main__":
    main()
