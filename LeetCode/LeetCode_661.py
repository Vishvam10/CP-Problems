"""
DIFFICULTY : easy
TAGS : array, matrix
"""
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        if rows < 1:
            return img
        dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                count = 1
                s = img[i][j]
                
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]
                    
                    if x < 0 or x >= rows:
                        continue
                    if y < 0 or y >= cols:
                        continue
                    
                    count += 1
                    s += img[x][y]
                    
                res[i][j] = s // count

        return res