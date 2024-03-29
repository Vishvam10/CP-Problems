class Solution:
    def insert(self, arr: List[List[int]], b: List[int]) -> List[List[int]]:
        arr.append(b)
        arr.sort(key=lambda x: x[0])
        ans = []

        for ele in arr:
            if (not ans or ele[0] > ans[-1][1]):
                ans.append(ele)
            else:
                ans[-1][1] = max(ans[-1][1], ele[1])

        return ans
