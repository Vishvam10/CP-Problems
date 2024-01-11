import heapq

class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        return heapq.nlargest(k, arr)[-1]
