class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        mat = [[0 for i in range(n)] for j in range(n)]
        x = 1
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        while (top <= bottom and left <= right):

            # go right
            for i in range(left, right+1):
                mat[top][i] = x
                x += 1

            top += 1

            # go down
            for i in range(top, bottom+1):
                mat[i][right] = x
                x += 1

            right -= 1

            if (top <= bottom):

                # go left
                for i in range(right, left-1, -1):
                    mat[bottom][i] = x
                    x += 1

                bottom -= 1

            if (left <= right):

                # go up
                for i in range(bottom, top-1, -1):
                    mat[i][left] = x
                    x += 1

                left += 1

        return mat
