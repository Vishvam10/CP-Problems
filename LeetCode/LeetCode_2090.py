"""
DIFFICULTY : medium
TAGS : array, sliding window
"""
class Solution:
    # Use prefix sums
    def getAverages(self, arr: List[int], k: int) -> List[int]:
        ans = [-1] * len(arr)
        left, s, dia = 0, 0, 2*k+1
        for right in range(len(arr)):
          s += arr[right]
          if (right - left + 1 >= dia):
            ans[left + k] = s // dia
            s -= arr[left]
            left += 1
        return ans