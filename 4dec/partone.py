from __future__ import annotations
from typing import NamedTuple

with open("input.txt") as file:
    first, *rest = file.read().split("\n\n")

class Board(NamedTuple):
    left: set[int]
    ints: list[int]

    @property
    def has_won(self) -> bool:
        for i in range(5):
            for j in range(5):
                if self.ints[i * 5 + j] in self.left:
                    break
            else:
                return True

            for j in range(5):
                if self.ints[i + 5 * j] in self.left:
                    break
            else:
                return True
        else:
            return False

    @classmethod
    def parse(cls, board: str) -> Board:
        ints = [int(s) for s in board.split()]
        left = set(ints)
        return cls(left, ints)

boards = [Board.parse(board) for board in rest]
ints = [int(s) for s in first.split(',')]

def get_number():
    for num in ints:
        for board in boards:
            board.left.discard(num)

        for board in boards:
            if board.has_won:
                return sum(board.left) * num

print(ints)
print(boards)
print(get_number())