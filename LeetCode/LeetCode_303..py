"""
DIFFICULTY : easy
TAGS : array, design, prefix sum
"""
class NumArray:

    def __init__(self, arr):
        self.pre = arr
        for i in range(1, len(arr)):
            self.pre[i] += self.pre[i-1]

    def sumRange(self, left, right):
        if(left > 0) :
            return self.pre[right] - self.pre[left-1]
        else :
            return self.pre[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)