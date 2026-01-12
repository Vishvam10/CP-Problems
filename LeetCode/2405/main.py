"""
DIFFICULTY : medium
TAGS : string, hash table, greedy
"""


class Solution:
    def partitionString(self, s: str) -> int:
        mp = {}
        ptr = 0
        ans = 1
        while ptr < len(s):
            if s[ptr] not in mp:
                mp[s[ptr]] = True
                ptr += 1
            else:
                mp.clear()
                ans += 1

        return ans
