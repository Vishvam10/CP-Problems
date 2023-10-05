class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        max_dist = float("inf")
        ind = -1
        for i in range(len(points)) :
            p = points[i]
            xc, yc = p[0], p[1]
            if(xc == x or yc == y) :
                dist = abs(xc - x) + abs(yc - y)
                if(dist < max_dist) :
                    max_dist = dist
                    ind = i
        return ind

        