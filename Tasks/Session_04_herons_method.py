#!/usr/bin/env python3
"""herons_method.py"""


def hm(s: float, p: float) -> str:
    """
    Input: \n
    s = the number whos square root you wish to approximate \n
    p = the amount of precision you would like for the approximation \n
    Output: \n
    m = is a string that contains the value of the approximation and other relevant information
    """

    # g = the initial guess for the square root of s
    g: float = s / 2

    # err = the error in the estimate
    # (it may yield a negative number, thus we use abs())
    err: float = abs(s - g**2)

    # i = number of iterations carried out
    i: int = 0

    while err >= p:
        # This formula is the result of herrons method
        g = ((s / g) + g) / 2

        err = abs(s - g**2)
        i += 1

    m: str = f" Number being approximated:   {s:,} \n Approximation:               {round(g,8):,} \n Error:                       {err:,} \n Number of iterrations:       {i:,}"

    return m


def main() -> None:
    s: float = 2
    p: float = 1e-8

    print(hm(s, p))


if __name__ == "__main__":
    main()
