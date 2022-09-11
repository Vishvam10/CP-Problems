class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in range(len(arr1)) :
            flag = False
            for j in range(len(arr2)) :
                if(abs(arr1[i] - arr2[j]) <= d) :
                    flag = True
            if(not flag) :
                ans += 1
        return ans