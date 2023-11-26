from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        left, ans = 0, 0
        mp = defaultdict(int)

        for i in range(n) :
            ch = s[i]
            mp[ch] += 1
            if(mp[ch] > 1) :       
                while(mp[ch] > 1) :
                    mp[s[left]] -= 1
                    left += 1
                
            ans = max(ans, i - left + 1)
        
        return ans
