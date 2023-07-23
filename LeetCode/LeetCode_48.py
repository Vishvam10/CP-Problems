class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(mat)
        left = 0
        right = n-1

        while(left <= right) :
            for it in range(right-left) :
                top = left
                bottom = right

                temp = mat[top][left+it]

                mat[top][left+it]        = mat[bottom-it][left]
                mat[bottom-it][left]     = mat[bottom][right-it]
                mat[bottom][right-it]    = mat[top+it][right]
                mat[top+it][right]       = temp

            left += 1
            right -= 1
        
        
