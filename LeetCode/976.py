class Solution:
    def largestPerimeter(self, arr: List[int]) -> int:
        # Reverse
        arr = sorted(arr)[::-1]
        for i in range(len(arr) - 2):
            if arr[i] < arr[i + 1] + arr[i + 2]:
                return arr[i] + arr[i + 1] + arr[i + 2]
        return 0