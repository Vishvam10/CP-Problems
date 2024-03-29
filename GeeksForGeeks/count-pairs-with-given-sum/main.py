
class Solution:
    def getPairsCount(self, arr, n, k):
        mp = {}
        count = 0
        for i in range(n):
            if arr[i] not in mp.keys():
                mp[arr[i]] = 1
            else:
                mp[arr[i]] += 1
        for i in range(n):
            if ((k - arr[i]) in mp):
                mp[arr[i]] -= 1
                count += mp[k - arr[i]]

        return count
