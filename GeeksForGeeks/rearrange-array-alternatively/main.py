class Solution:
    # Complete this function
    # Function to rearrange  the array elements alternately.
    def rearrange(self, arr, n):
        min_ele = arr[0]
        max_ele = arr[n-1] + 1
        min_ind = 0
        max_ind = n-1
        for i in range(n):
            if (i % 2 == 0):
                arr[i] += (arr[max_ind] % max_ele) * max_ele
                max_ind -= 1
            else:
                arr[i] += (arr[min_ind] % max_ele) * max_ele
                min_ind += 1
        for i in range(n):
            arr[i] //= max_ele
        return arr
