class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s) > len(t)) :
            return False
        if(len(s) == 0) :
            return True
        i = 0
        for j in range(len(t)) :
            if(i <= len(s) - 1) :
                if(s[i] == t[j]) :
                    i += 1
        return i == len(s)