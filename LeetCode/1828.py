"""
DIFFICULTY : medium
TAGS : array, math, geometry
"""
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x,y,r in queries:
            count = 0
            for a,b in points:
                if (x-a)*(x-a) + (y-b)*(y-b) <= r*r:
                    count += 1
            ans.append(count)
        return ans