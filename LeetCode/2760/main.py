class Solution:
    def longestAlternatingSubarray(self, arr: List[int], thresh: int) -> int:

        n = len(arr)
        c, prev, ans = 0, 0, 0

        for i in range(n) :

            if((c > 0) and (arr[i] & 1) != (prev & 1) and (thresh >= arr[i])) :
                c += 1
            else :
                c = int((thresh >= arr[i]) and (arr[i] & 1 == 0))
            
            ans = max(ans, c)
            prev = arr[i]
        
        return ans


        