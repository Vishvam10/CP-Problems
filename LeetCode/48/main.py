class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(mat)
        left = 0
        right = n-1

        while (left <= right):
            for level in range(right-left):
                top = left
                bottom = right

                temp = mat[top][left+level]

                mat[top][left+level] = mat[bottom-level][left]
                mat[bottom-level][left] = mat[bottom][right-level]
                mat[bottom][right-level] = mat[top+level][right]
                mat[top+level][right] = temp

            left += 1
            right -= 1
