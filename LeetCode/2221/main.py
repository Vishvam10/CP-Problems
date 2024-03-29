"""
DIFFICULTY : medium
TAGS : array, math, simulation, combinatorics
"""


class Solution:
    def triangularSum(self, arr: List[int]) -> int:
        # Using pascal triangle and binomial coefficients
        # total = sum over all k in {1 .. k} (nCk)a_k
        # where a_k is the element at index k and n = len(arr) - 1
        #
        # To calculate nCk effectively :
        # nCk = nCk-1 * x for some x. Solving for x, we get
        # x = n - k + 1 / k
        # So, nCk = nCk-1 * (n-k+1)/k
        # Now, we can calculate nCk as we iterate through the list in O(1) time

        for i in range(len(arr)):
            coef = 1
            total = arr[0]
            n = len(arr) - 1
            for k in range(1, len(arr)):
                coef *= (n - k + 1)
                coef //= k  # Integer division to avoid floating point
                total += coef * arr[k]
                total %= 10
            return total
