"""
DIFFICULTY : easy
TAGS : array, hash table
"""


class Solution:
    def unequalTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (arr[i] != arr[j] and arr[i] != arr[k] and arr[j] != arr[k]):
                        ans += 1
        return ans
