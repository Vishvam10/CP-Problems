import copy
class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k %= n
        cpy = copy.deepcopy(arr)
        for i in range(n) :
            arr[(i+k)%n] = cpy[i]
        return arr