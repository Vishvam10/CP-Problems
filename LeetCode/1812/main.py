"""
DIFFICULTY : easy
TAGS : math, string
"""


class Solution:
    # a = 97 in ascii. We want 1-based indexing so
    # subtract 96 instead of 97
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = int(ord(coordinates[0]) - 96), int(coordinates[1])
        if x % 2 == 0:
            if y % 2 == 0:
                return False
            else:
                return True
        else:
            if y % 2 == 1:
                return False
            else:
                return True
        return False
