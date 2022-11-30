"""
DIFFICULTY : easy
TAGS : two pointers, string
"""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a = 0
        b = 0
        
        while(b < len(typed)) :
            if(a < len(name) and name[a] == typed[b]) :
                a += 1
                b += 1
            elif(a > 0 and name[a-1] == typed[b]) :
                b += 1
            else :
                return False
        
        if(a == len(name)) :
            return True
        
        return False