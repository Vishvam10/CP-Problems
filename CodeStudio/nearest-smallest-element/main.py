class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):

        n = len(arr)
        ans = [-1] * n

        smallest = arr[0]

        for i in range(1, n):

            if (arr[i] > smallest):
                ans[i] = smallest
            else:
                ans[i] = -1
                smallest = arr[i]

        return ans
