"""
DIFFICULTY : basic
TAGS : array, sorting
"""
# User function Template for python3


class Solution:

    def maxProduct(self, arr, n):
        # code here
        arr.sort()

        s1 = arr[0] * arr[1]
        s2 = arr[n-1] * arr[n-2]

    return max(s1, s2)
