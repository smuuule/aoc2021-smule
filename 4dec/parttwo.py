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
    last = -1
    seen = set()
    for num in ints:
        for board in boards:
            board.left.discard(num)

        for i, board in enumerate(boards):
            if i not in seen and board.has_won:
                last = sum(board.left) * num
                seen.add(i)

    return last

print(ints)
print(boards)
print(get_number())