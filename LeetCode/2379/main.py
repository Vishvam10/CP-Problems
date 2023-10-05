"""
DIFFICULTY : easy
TAGS : string, sliding window
"""
class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        s = list(s)
        ans = float("inf")
        for i in range(len(s)) :
            sub_string = s[i:i+k]
            if(len(sub_string) == k) :
                count = 0
                for ch in sub_string :
                    if(ch == "W") :
                        count += 1
                ans = min(ans, count)
            
        return ans