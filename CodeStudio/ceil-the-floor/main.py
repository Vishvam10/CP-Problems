class Solution:
    def searchRange(self, arr: List[int], x: int) -> List[int]:
        n = len(arr)

        def start():
            low, high, ans = 0, n - 1, -1
            while (low <= high):
                mid = low + (high - low) // 2
                if (arr[mid] == x):
                    ans = mid
                    high = mid - 1
                elif (arr[mid] < x):
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        def end():
            low, high, ans = 0, n - 1, -1
            while (low <= high):
                mid = low + (high - low) // 2
                if (arr[mid] == x):
                    ans = mid
                    low = mid + 1
                elif (arr[mid] < x):
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        return [start(), end()]
