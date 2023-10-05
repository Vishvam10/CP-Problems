class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        n = len(arr)
        if(n == 0) :
            return 0
        if(n == 1) :
            return 1
        
        # mp = {} is slower in lookup, so a set()
        mp = set()
        ans = 1

        for i in range(n) :
            mp.add(arr[i])
        
        for start in mp :
            if(start - 1 not in mp) :
                c = 1
                temp = start
                while(temp + 1 in mp) :
                    c += 1
                    temp += 1
                    
                ans = max(ans, c)
        
        return ans