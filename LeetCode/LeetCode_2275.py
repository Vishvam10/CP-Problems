"""
DIFFICULTY : medium
TAGS : array, hash table, bit manipulation, counting
"""
class Solution:
    def largestCombination(self, arr: List[int]) -> int:
        n = len(bin(max(arr))[2:])
        mp = [0] * n
        for i in range(len(arr)) :
            b = bin(arr[i])[2:].zfill(n)
            for j in range(len(b)) :
                if(b[j] == "1") :
                    mp[j] += 1
        return max(mp)