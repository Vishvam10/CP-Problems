class Solution:
    def maximumGap(self, arr: List[int]) -> int:
        
        if(len(arr) < 2) :
            return 0

        mx, mn, n = max(arr), min(arr), len(arr)
        if(mx == mn) :
            return 0
        
        bucket_size = max(1, ((mx - mn) // (n - 1)))
        n_buckets = ((mx - mn) // bucket_size) + 1
        
        buckets = [
            [float('inf'), float('-inf')] for _ in range(n_buckets)
        ]
        
        for x in arr :
            # x = mn + (ind * bucket_size)
            ind = (x - mn) // bucket_size
            buckets[ind][0] = min(buckets[ind][0], x)
            buckets[ind][1] = max(buckets[ind][1], x)

        ans = 0
        prev = buckets[0][1]

        # Max interval between consecutive buckets

        for i in range(1, n_buckets) :
            if(buckets[i][0] == float("inf")) :
                continue
            ans = max(ans, buckets[i][0] - prev)
            prev = buckets[i][1]

        return ans