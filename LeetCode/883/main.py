"""
DIFFICULTY : easy
TAGS : array, math, geometry, matrix
"""
class Solution:
    # IDEA : Max rows and max columns
    # front-back projection area on xz = sum(max value for every col)
    # right-left projection area on yz = sum(max value for every row)
    # top-down projection area on xy   = sum(1 for every v > 0)

    def projectionArea(self, arr: List[List[int]]) -> int:
        n = len(arr)
        ans = 0
        
        for i in range(n) :
            yz_plane_area, xz_plane_area, xy_plane_area = 0, 0, 0
            for j in range(n) :
                yz_plane_area = max(yz_plane_area, arr[i][j])
                xz_plane_area = max(xz_plane_area, arr[j][i])
                if(arr[i][j]) :
                    xy_plane_area += 1
                    
            ans += (yz_plane_area + xz_plane_area + xy_plane_area)
        
        return ans