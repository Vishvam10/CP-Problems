"""
DIFFICULTY : medium
TAGS : array, searching, mathematical
"""


class Solution:
    def closestToZero(self, arr, n):
        # your code here
        arr.sort()
        l = 0
        r = n - 1
        s = arr[0] + arr[n-1]
        while (l < r):
            temp = arr[l] + arr[r]
            if (temp == 0):
                return 0
            if (temp < 0):
                l += 1
            else:
                r -= 1

            if (abs(temp) < abs(s)):
                s = temp
            if (abs(temp) == abs(s)):
                s = max(s, temp)

        return s
