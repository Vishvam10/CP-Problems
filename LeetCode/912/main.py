class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:

        def merge(arr, left, mid, right):
            i, j = left, mid + 1
            ans = []

            while (i <= mid and j <= right):
                if (arr[i] < arr[j]):
                    ans.append(arr[i])
                    i += 1
                else:
                    ans.append(arr[j])
                    j += 1

            while (i <= mid):
                ans.append(arr[i])
                i += 1

            while (j <= right):
                ans.append(arr[j])
                j += 1

            # overwrite

            for i in range(len(ans)):
                arr[i + left] = ans[i]

            return arr

        def mergeSort(arr, left, right):
            if (left >= right):
                return

            mid = left + (right - left) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)
            ans = merge(arr, left, mid, right)

            return ans

        ans = mergeSort(arr, 0, len(arr) - 1)
        return ans
