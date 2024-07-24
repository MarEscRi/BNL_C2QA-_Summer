#!/usr/bin/env python3
"""board_encoding.py"""

from typing import Any


def bd(n: int) -> Any:
    """
    Function takes in Non-zero integers
    """

    # In order to have the value of n at the end
    N: int = n

    # the algorithm for finding the base 3 representation of an integer
    r: int = 0
    n3: str = ""
    while n > 0:
        n, r = divmod(n, 3)
        n3 = str(r) + n3

    # All 9 spaces on the board must be filled
    if len(n3) < 9:
        while len(n3) != 9:
            n3 = str(0) + n3

    # Since there are only 9 spaces on the board n3 can only have 9 digits
    if len(n3) > 9:
        return print(
            "The integer provided can not be used to represent a tic tac tow board"
        )

    # The str changed into a list
    b: list[str] = list(n3)

    # Printing the board
    return print("Board Number: ", N, "\n", b[0:3], "\n", b[3:6], "\n", b[6:9])


def main() -> None:
    bd(2271)
    bd(1638)
    bd(12065)


if __name__ == "__main__":
    main()
