"""
DIFFICULTY : easy
TAGS : array, hash table, sliding window
"""
class Solution:
    def containsNearbyDuplicate(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        mp = {}
        
        for i in range(n) :
            if(arr[i] in mp) :
                diff = mp[arr[i]] - i
                if(abs(diff) <= k) :
                    return True
                else :
                    mp[arr[i]] = i
            else :
                mp[arr[i]] = i
        
        return False