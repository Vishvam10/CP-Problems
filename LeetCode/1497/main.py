class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        mp = defaultdict(int)

        for i in range(len(arr)):
            # if(arr[i] < 0) :
            #     arr[i] = k - (abs(arr[i]) % k)
            # else :
            arr[i] %= k
            mp[arr[i]] += 1

        for i in range(len(arr)):
            target = k - arr[i]

            if (arr[i] == 0):
                if (arr[i] in mp and mp[arr[i]] >= 1):
                    mp[arr[i]] -= 2
                elif (target in mp and mp[target] >= 1):
                    mp[arr[i]] -= 1
                    mp[target] -= 1

            if (target in mp and mp[target] >= 1):
                mp[arr[i]] -= 1
                mp[target] -= 1

        for v in mp.values():
            if (v != 0):
                return False

        return True
