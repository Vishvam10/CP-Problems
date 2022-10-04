class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        ans = [0] * len(cost)
        ans[0] = cost[0]
        if len(cost) >= 2:
            ans[1] = cost[1]
        for i in range(2, len(cost)) :
            ans[i] = cost[i] + min(ans[i-1], ans[i-2])
        return min(ans[-1], ans[-2])