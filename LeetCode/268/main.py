"""
DIFFICULTY : easy
TAGS : array, hash table, sorting, binary search, bit manipulatiom, math
"""


class Solution:
    # ALTERNATE : Apply XOR operation to
    # both the index and value of the array.
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        return n * (n+1) // 2 - sum(arr)
