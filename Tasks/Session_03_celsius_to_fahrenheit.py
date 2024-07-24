#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""

# I have based this program off of the code found in "fahrenheit_to_celsius.py"

def main() -> None:
    # f = temperature in fahrenheit 
    # c = temperature in celsius

    for c in range(-44, 106 + 1, 4):

        # Formula for converting from celsius to fahrenheit 
        f: float = (9 / 5) * c + 32

        print(f"{c:>6.2f} C = {f:>6.2f} F" )

if __name__ == "__main__":
    main()

#   On the subject of the end point for the range
# assuming this was a task handed from a scientist to a programmer, as a programmer 
# I believe it would be wise to assume that the scientist has used certain principals, 
# laws, educated guesses, etc... in order to deduce the neccesary range for the calculations.
# The scientist has deduced that values outside the given range are not neccesary 
# and therefore expanding the range would add uneccesary data, 
# thus possibly extending 
# the time required for the calculations (causing a delay on the scientists work)
# and occupying more space.  