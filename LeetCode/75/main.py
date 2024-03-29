class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        p1 = 0
        cur = 0
        p3 = n - 1

        while (cur <= p3):
            if (arr[cur] == 0):
                arr[p1], arr[cur] = arr[cur], arr[p1]
                cur += 1
                p1 += 1
            elif (arr[cur] == 1):
                cur += 1
            elif (arr[cur] == 2):
                arr[p3], arr[cur] = arr[cur], arr[p3]
                p3 -= 1
