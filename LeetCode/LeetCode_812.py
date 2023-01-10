"""
DIFFICULTY : easy
TAGS : array, math, geometry
"""
class Solution:
    def largestTriangleArea(self, pts: List[List[int]]) -> float:
        n = len(pts)
        ans = 0
        for i in range(n):
            x1,y1 = pts[i]
            for j in range(i+1,n):
                x2,y2 = pts[j]
                for k in range(j+1,n):
                    x3,y3 = pts[k]
                    temp = abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                    if temp > ans:
                        ans = temp
        return ans
        