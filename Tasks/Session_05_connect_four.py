#!/usr/bin/env python3
"""connect_four.py"""

import typing

import numpy as np

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def print_winner(board:  list[list[int]]) -> None:
    b: NDArray[np.int_] = np.array(board)
    B: NDArray[np.int_] = np.flipud(b) 

    for i in range(len(B[:,0]) - 3):
        for j in range(len(B[0,:]) - 3 ):
            
            # Horizontal victory 

            # p1 
            if B[i,j] == B[i,j + 1] == B[i,j + 2] == B[i,j + 3] == 1: 
                print("Player 1 wins with a horizontal victory!")
            # p2
            if B[i,j] == B[i,j + 1] == B[i,j + 2] == B[i,j + 3] == 2: 
                print("Player 2 wins with a horizontal victory!")

            # Vertical victory 

            # p1 
            if B[i,j] == B[i + 1,j] == B[i + 2,j] == B[i + 3,j] == 1: 
                print("Player 1 wins with a vertical victory!")
            # p2
            if B[i,j] == B[i + 1,j] == B[i + 2,j] == B[i + 3,j] == 2: 
                print("Player 2 wins with a vertical victory!")
            
            # Diagonal victory 

            # p1 
            if B[i,j] == B[i + 1,j + 1] == B[i + 2,j + 2] == B[i + 3,j + 3] == 1: 
                print("Player 1 wins with a diagonal victory!")
            # p2
            if B[i,j] == B[i + 1,j + 1] == B[i + 2,j + 2] == B[i + 3,j + 3] == 2: 
                print("Player 2 wins with a diagonal victory!")

            # Off Diaginal victory 
            # p1
            if b[i,j] == b[i + 1,j + 1] == b[i + 2,j + 2] == b[i + 3,j + 3] == 1: 
                print("Player 1 wins with an off diagonal victory!")
            # p2
            if b[i,j] == b[i + 1,j + 1] == b[i + 2,j + 2] == b[i + 3,j + 3] == 2: 
                print("Player 2 wins with an off diagonal victory!")

    print(*board, sep="\n")
    print()



def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()

# This code can be made more efficiant by making it such that 
# if the entry b[i,j] = 0 then dont check for the victories 