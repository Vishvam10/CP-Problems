class Solution:
    def average(self, arr: List[int]) -> float:
        return (sum(arr) - max(arr) - min(arr)) / (len(arr) - 2)
