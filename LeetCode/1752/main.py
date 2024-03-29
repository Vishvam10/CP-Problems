class Solution:
    def check(self, arr: List[int]) -> bool:
        n = len(arr)
        c = 0
        ind = -1
        for i in range(1, n, 1):
            if (arr[i-1] <= arr[i]):
                continue
            else:
                c += 1
                ind = i-1

        if (c > 1):
            return False

        if (ind == -1):
            return True

        # ind is the rotation index
        # arr[ind+1:n] + arr[0:c] should be sorted

        temp = arr[ind+1:n] + arr[:ind+1]

        for i in range(1, n, 1):
            if (temp[i-1] <= temp[i]):
                continue
            else:
                return False

        return True
