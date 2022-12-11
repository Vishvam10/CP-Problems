"""
DIFFICULTY : easy
TAGS : hash table, string, counting
"""
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mp = {}
        for ch in s :
            if(ch not in mp) :
                mp[ch] = 1
            else :
                mp[ch] += 1
        temp = mp[s[0]]
        for v in mp.values() :
            if(v != temp) :
                return False
        return True
        