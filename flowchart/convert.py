from dataclasses import dataclass
import re
from typing import List, Optional

path = "M5.88 46.5C3.542 46.5 1 40.071 1 31.5s2.542-15 4.88-15h51.24c-2.44 0-4.88 6.429-4.88 15s2.44 15 4.88 15z"
all_matches = re.finditer("[A-Za-z][-\d. ]*", path)


@dataclass
class Position:

    x: float
    y: float


@dataclass
class Bezier:

    x1: float
    y1: float

    x2: float
    y2: float

    x: float
    y: float

    def from_s(self, x2: float, y2: float, x: float, y: float):
        return Bezier(
            2*self.x - self.x2,
            2*self.y - self.y2,
            x2, y2, x, y)


# position = Position(next(all_matches).group(0))
# print(position)
# position.update(next(all_matches).group(0))
# print(position)

position: Position
bezier: Optional[Bezier] = None

for match in all_matches:
    full_command: str = match.group(0).replace("-", " -")
    command: str = full_command[0]
    nums: List[float] = [float(m) for m in full_command[1:].split()]

    if command == "M":
        bezier = None
        position = Position(*nums)
    elif command == "C":
        bezier = Bezier(*nums)
        position = Position(bezier.x, bezier.y)
    elif command == "s":
        bezier = bezier.from_s(*nums)
        position = Position(bezier.x, bezier.y)
    else:
        raise ValueError(command + " not defined")
    print()
    print(position)
    print(bezier)
