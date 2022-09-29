class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
        n = len(arr)
        left, max_len = 0, 0
        mp = {}
        for i in range(n) :
            if(arr[i] in mp and left <= mp[arr[i]]) :
                left = mp[arr[i]] + 1
            else :
                max_len = max(max_len, i - left + 1)
            mp[arr[i]] = i
            
        return max_len