class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        
        n = len(arr)
        left, s, ans = 0, 0, 0

        for i in range(n) :
            s += arr[i]
            ws = i - left + 1
            if(ws > k) :
                s -= arr[left]
                left += 1
            elif(ws == k) :
                ans = max(ans, s / ws)

        return ans            
