class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        s = sum(arr[0:k-1])
        left, ans = 0, 0

        for i in range(k-1, n, 1) :

            s += arr[i]
            avg = s / k

            if(avg >= threshold) :
                ans += 1
            
            s -= arr[left]
            left += 1

        return ans
            