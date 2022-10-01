class Solution:
    # 2 loops is obvious. The main idea is to 
    # RESTRICT the axes. Just traverse in 1 
    # direction and figure out the other one 
    # using the first. 
    
    # Primary diagonal : i == j
    # Secondary diagonal : i + j = n - 1
    
    # Instead of using j, force the element to be 
    # either : mat[i][i] or mat[i][n-i-1] where 
    # n = len(mat)
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        # for i in range(len(mat)) :
        #     for j in range(len(mat[0])) :
        #         if(i == j) :
        #             ans += mat[i][j]
        #         elif(i + j == n - 1) :
        
        for i in range(n) :
            if(2*i == n - 1) :
                ans += mat[i][i]
            else :
                ans += (mat[i][i] + mat[i][n - i - 1])
        
        return ans
        