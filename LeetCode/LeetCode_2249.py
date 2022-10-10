class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for x,y,r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (x - i) ** 2 + (y - j) ** 2 <= r * r:
                        res.add((i,j))
        return len(res)
        