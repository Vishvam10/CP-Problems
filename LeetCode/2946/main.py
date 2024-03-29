class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        # def rshift(arr, k) :
        #     n = len(arr)
        #     k %= n
        #     return arr[-k:] + arr[:n-k]

        # def lshift(arr, k) :
        #     n = len(arr)
        #     k %= n
        #     return arr[k:] + arr[:k]

        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if (i % 2 == 0):
                    # if (j-k) < 0, then just add n else leave it as it is
                    if (mat[i][j] != mat[i][(j-k+n) % n]):
                        return False
                else:
                    if (mat[i][j] != mat[i][(j+k) % n]):
                        return False

        return True
