class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, n, k):
        for i in range(0, n, k):
            if i > n - k:
                arr[i:] = reversed(arr[i:])
            else:
                arr[i : i + k] = reversed(arr[i : i + k])

    return arr
