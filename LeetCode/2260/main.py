class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp = {}
        min_diff = float("inf")

        for i in range(len(cards)):
            c = cards[i]
            if c in mp:
                min_diff = min(min_diff, i - mp[c] + 1)
            mp[c] = i

        if min_diff == float("inf"):
            return -1
        return min_diff
