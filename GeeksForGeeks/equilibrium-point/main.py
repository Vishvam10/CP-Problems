class Solution:
    # Complete this function
    #
    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, arr, n):
        total = sum(arr)
        sum_before = 0
        eq_pt = 0
        for i in range(len(arr)):
            # Total sum - equilibrium_point = 2 * sum_before
            if (total - (sum_before + arr[i]) == sum_before):
                return eq_pt + 1
            else:
                eq_pt += 1
                sum_before += arr[i]
        return -1
