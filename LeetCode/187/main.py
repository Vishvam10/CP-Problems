from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        mp = defaultdict(int)
        ans = []

        for i in range(n+1):
            substr = s[i:i+10]
            if (mp[substr] != -1):
                mp[substr] += 1
            if (mp[substr] > 1):
                ans.append(substr)
                mp[substr] = -1

        return ans
