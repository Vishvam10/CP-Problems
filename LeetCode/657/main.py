"""
DIFFICULTY : easy
TAGS : string, simulation
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        n_up, n_down, n_left, n_right = 0, 0, 0, 0
        for ch in moves :
            if(ch == "L") :
                n_left += 1
            elif(ch == "R") :
                n_right += 1
            elif(ch == "U") :
                n_up += 1
            else :
                n_down += 1
        if(n_left == n_right and n_up == n_down) :
            return True
        return False
        