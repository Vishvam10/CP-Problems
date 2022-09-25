class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}
        
        for ch1, ch2 in zip(s, t) :
            if((ch1 not in mp1) and (ch2 not in mp2)) :
                mp1[ch1] = ch2
                mp2[ch2] = ch1
            elif((mp1.get(ch1) != ch2) or (mp2.get(ch2) != ch1)) :
                return False
        
        return True