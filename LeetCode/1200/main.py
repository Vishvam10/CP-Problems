class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        min_diff = float('inf')

        arr.sort()

        for i in range(len(arr) - 1) :
            min_diff = min(min_diff, abs(arr[i] - arr[i+1]))

        for i in range(len(arr) - 1) :
            if(abs(arr[i] - arr[i+1]) == min_diff) :
                ans.append([arr[i], arr[i+1]])

        return ans