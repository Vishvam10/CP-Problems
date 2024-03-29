from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1

        for (ch, freq) in sorted(mp.items(), key=lambda kv: (-kv[1], kv[0])):
            ans += (freq * ch)

        return ans
