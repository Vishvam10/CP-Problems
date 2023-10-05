class Solution:
    def xorAllNums(self, A: List[int], B: List[int]) -> int:
        x = y = 0
        for a in A:
            x ^= a
        for b in B:
            y ^= b
        return (len(A) % 2 * y) ^ (len(B) % 2 * x)
        