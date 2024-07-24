#!/usr/bin/env python3
"""sum_squares.py"""


def main() -> None:
    # n = the number you wish to sum to
    # s = the value of the sum

    n: int = 1_900
    s: float = 0.0

    for i in range(1, n):
        if i % 7 == 0 and i % 11 == 0:
            s += i

    print(
        f"The following is the sum of all natural numbers less than",
        f"{n:,.0f}",
        f"that are divisible by 7 and 11 ",
    )
    print(f"{s:,.0f}")


if __name__ == "__main__":
    main()
