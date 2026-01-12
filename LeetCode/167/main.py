class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] > target:
                right -= 1
            elif arr[left] + arr[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return -1
