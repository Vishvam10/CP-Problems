"""
DIFFICULTY : medium
TAGS : array, dp, greedy
"""


class Solution:
    # The action we can do on ith day is either buy
    # (if last action is sell), or sell (if last action
    # is buy), or do nothing (not buy, not sell).
    def maxProfit(self, arr: List[int]) -> int:
        curBuy = float("-inf")
        curSold = float("-inf")
        lastBuy = -arr[0]
        lastSold = 0
        n = len(arr)
        if (n == 0):
            return 0
        for i in range(1, n):
            curBuy = max(lastBuy, lastSold - arr[i])
            curSold = max(lastSold, lastBuy + arr[i])
            lastBuy = curBuy
            lastSold = curSold
        return lastSold
