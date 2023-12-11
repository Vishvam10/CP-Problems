class Solution:
    def numIdenticalPairs(self, arr: List[int]) -> int:
        
        ans = 0

        for i in range(len(arr)) :
            for j in range(i+1, len(arr)) :
                if(arr[i] == arr[j]) :
                    ans += 1
            
        return ans