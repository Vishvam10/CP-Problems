"""
DIFFICULTY : easy
TAGS : array, matrix
"""


class Solution:
    # *matrix decomposes it into separate lists
    # each representing a row for example if
    # matrix =[[1,2], [3, 4]] then *matrix
    # returns two lists [1,2] and [3, 4]
    # zip([1, 2], [3, 4]) returns two lists of
    # [1, 3] and [2, 4] which are the columns of the matrix
    # & between two sets min_r and max_c returns
    # the intersection of two sets

    def luckyNumbers(self, mat: List[List[int]]) -> List[int]:
        min_r = {min(r) for r in mat}
        max_c = {max(c) for c in zip(*mat)}
        return list(min_r & max_c)
