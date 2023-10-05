class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, arr, n):
        flag = False
        ans = []
        max_ele = -100000000
        for i in range(n-1, -1, -1):
            if(arr[i] >= max_ele):
                ans.append(arr[i])
                max_ele = arr[i]
        ans.reverse()
        return ans
