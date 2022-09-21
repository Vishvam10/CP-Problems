class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack)) :
            s = haystack[i:i+n]
            if(needle == s) :
                return i
        return -1