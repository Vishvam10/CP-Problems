"""
DIFFICULTY : medium
TAGS : array, bit manipulation, prefix sum
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []

        for i in range(len(arr) - 1):
            arr[i + 1] ^= arr[i]

        for i,j in queries :
            if(i != 0) :
                ans.append(arr[j] ^ arr[i-1])
            else :
                ans.append(arr[j])
                
        return ans
        