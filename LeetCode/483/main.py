class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        for digits in range(64, 2, -1):
            low, high = 2, n - 1

            while (low <= high):

                mid = low + (high - low) // 2
                val = ((mid ** digits) - 1) // (mid - 1)

                if (val == n):
                    return str(mid)
                elif (val < n):
                    low = mid + 1
                else:
                    high = mid - 1

        return str(n - 1)
