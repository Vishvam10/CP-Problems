"""
DIFFICULTY : easy
TAGS : string, greedy
"""
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1, m1 = current.split(":")
        h1 = int(h1) 
        m1 = int(m1)
        cur_time = 60*h1 + m1

        h2, m2 = correct.split(":")
        h2 = int(h2) 
        m2 = int(m2)
        cor_time = 60*h2 + m2

        diff = abs(cor_time - cur_time)
        ans = 0
        i = 0
        allowed = [60, 15, 5, 1]
        while(diff > 0) :
            if(diff >= allowed[i]) :
                diff -= allowed[i]
                ans += 1
            else :
                i += 1
        return ans




