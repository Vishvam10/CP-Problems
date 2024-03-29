"""
DIFFICULTY : easy
TAGS : array, math, simulation
"""


class Solution:
    # We only want the count, so all we need to do is
    # record whenever an odd row or column OCCURS. We
    # can use a boolean array with XOR 1 to do so. The
    # final answer can be calculated as :

    # count += 1 if (i XOR j == 1) for all i in m and j in n

    # We can further optimize it by having 2 more variables
    # to calculate the count as we go along the loop using the
    # formula :

    # odd_cols * even_rows + even_cols * odd_rows

    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # row = [False] * m
        # col = [False] * n
        # count = 0
        # for r in row :
        #     for c in col :
        #         if(r ^ c == 1) :
        #             count += 1
        # return count

        row, col = [False] * m, [False] * n
        for r, c in indices:
            row[r], col[c] = row[r] ^ True, col[c] ^ True
        odr, odc = sum(row), sum(col)
        return odr * (n - odc) + odc * (m - odr)
