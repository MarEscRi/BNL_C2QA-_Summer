#!/usr/bin/env python3
"""hamming_weight.py"""


def hw(n: int) -> int:
    """
    provides the sum of all the 1's in the binary representation of n (hamming weight) \n
    uses bin() function to do so 
    """

    # s = the binary representation of n as a string
    s: str = bin(n)[2:]

    # hw = the hamming weight
    hw: int = 0

    # Loop that adds all the digits of the binary representation
    for i in range(len(s)):
        hw += int(s[i])

    return hw

def hw2(n: int) -> int:
    """
    provides the sum of all the 1's in the binary representation of n (hamming weight) \n
    uses simple while loop and remainders
    """

    # s = hamming weight
    s = 0

    while n:
        s += n % 2 
        n >>= 1  

    return s

def main() -> None:
    n: int = 95601
    print(f"The hamming weight of {n:,} is {hw2(n):,}. the calulation was done using simple while loop and remainders")
    print(f"The hamming weight of {n:,} is {hw(n):,}. The calculation was done using 'bin()' function")


if __name__ == "__main__":
    main()
